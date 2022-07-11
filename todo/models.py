from django.db import models


class Task(models.Model):
    SEGMENT_CHOICES = (
        ("Y", "Done"),
        ("N", "Not Done")
    )

    content = models.CharField(max_length=255)
    datatime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    progress = models.CharField(
        max_length=1,
        choices=SEGMENT_CHOICES,
        default="N",
    )
    tags = models.ManyToManyField("Tag", related_name="tags")

    class Meta:
        ordering = ["progress", "-datatime" ]

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


