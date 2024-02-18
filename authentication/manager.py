from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, phone, password = None, **extra_fields):
        if not phone:
            raise ValueError("Phone Number is Required")
        # if not email:
        #     raise ValueError("Email is Required")
        
        # extra_fields['email']=self.normalize_email(extra_fields['email'])
        # email=self.normalize_email(email)
        user = self.model(phone=phone,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        return self.create_user(phone, password, **extra_fields)
    
        

