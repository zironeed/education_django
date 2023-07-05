from django import template

register = template.Library()


@register.filter(name="mediapath")
def get_media_path(image_path):

    if image_path:
        return f"/media/{image_path}"

    return 'No image'


@register.simple_tag(name="mediapath_tag")
def get_media_path_tag(image_path):

    if image_path:
        return f"/media/{image_path}"

    return 'No image'
