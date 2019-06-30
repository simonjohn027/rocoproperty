from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import  reverse
from .properties import houses,lease,rooms



class Property(models.Model):
    owner = models.CharField(max_length= 2000)
    location = models.CharField(max_length= 255, verbose_name="Location",blank= False)
    type = models.CharField(choices= houses,max_length= 25, verbose_name="Type of Property")
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    area = models.IntegerField(verbose_name="Total Area in Sq")
    room_number = models.IntegerField(verbose_name="Total Number of Rooms")
    availability = models.DateField(verbose_name="Available From")
    slug = models.SlugField(unique= True, max_length=20,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s ' % (self.type, self.location)

    def get_absolute_url(self):
        return reverse("main:property", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-created_on"]

def slug_create(instance, new_slug = None):
    slug = slugify(instance.project_name)
    if new_slug is not None:
        slug = new_slug
    qs = Property.objects.filter(slug = slug).order_by('-id')
    exist =qs.exists()
    if exist:
        new_slug = "%s-%s"%(slug,qs.first().id)
        return slug_create(instance,new_slug = new_slug)
    return slug


def presave_property_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slug_create(instance)


pre_save.connect(sender= Property,receiver= presave_property_receiver)

class Room(models.Model):
    property = models.ForeignKey(Property, on_delete= models.CASCADE,related_name='rooms')
    room_type = models.CharField(max_length= 40, choices= rooms)
    room_size = models.IntegerField(verbose_name="Room Size in Sq")
    total = models.IntegerField(verbose_name="Number of this Room")

    class Meta:
        ordering = ['room_size']

    def __str__(self):
        return '%s - %s ' % (self.property, self.room_type)

class Image(models.Model):
    property = models.ForeignKey(Property,on_delete= models.CASCADE,related_name='images')
    file = models.ImageField(upload_to='upload')
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return '%s - %s ' % (self.property, self.file)

class Price(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    lease = models.CharField(max_length=25, choices=lease,verbose_name="Lease Type")
    price = models.IntegerField(verbose_name="Lease Price")


