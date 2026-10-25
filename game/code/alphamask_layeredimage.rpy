################################################################################
## An expansion of LayeredImageProxy to support AlphaMask, foregrounds,
## and backgrounds.
##
## Example:
# image eileen cutin = LayeredImageMask("eileen",
#     Transform(crop=(230, 0, 564, 953)),
#     mask="sprite_mask.png",
#     foreground="sprite_mask_frame.png",
#     background="sprite_bg.png"
# )
##
## This works like a normal LayeredImageProxy to start.
## `mask` is used as the mask argument for AlphaMask. It is an image.
## It is applied after the transforms are. Generally, you should use the
## transforms to make your sprite the same size as the mask, through cropping
## and/or zooming. Crop is used here (the mask is 564x953). You can also use
## the first two crop arguments to move your sprite around so it fits in the
## mask properly.
##
## `foreground` and `background` are properties applied to the final window
## the image appears in. Use these to add UI elements behind/in front
## of the sprite, or to add additional positioning properties. It takes any
## other properties that a Window takes as well, including size and position.
## Foreground and background images should be the same size as your mask for
## best results.
##
## If you use this code in your project,
## please credit me as Feniks @ feniksdev.com
## Also consider tossing me a ko-fi @ https://ko-fi.com/fen
################################################################################
init offset = -100

python early in layeredimage:

    from store import AlphaMask, Window

    class LayeredImageMask(LayeredImageProxy):
        """
        This is an image-like object that proxies attributes passed to it to
        another layered image. It allows for the use of transforms and alpha
        masks.

        `name`
            A string giving the name of the layeredimage to proxy to.

        `transform`
            If given, a transform or list of transforms that are applied to the
            image after it has been proxied.

        `mask`
            If given, a mask image which is applied on the transformed
            layeredimage proxy using :ref:`AlphaMask`. The layeredimage proxy
            is provided as the child to the AlphaMask and this argument as the
            mask.

        `properties`
            Optional properties which will be applied to the final Window
            displayable with the masked image. Can be used to set a default
            position in a particular corner, for example, or add a foreground
            and background.
        """

        def __init__(self, name, transform=None, mask=None, **properties):

            super(LayeredImageMask, self).__init__(name, transform)

            self.mask = mask
            self.properties = properties
            self.style = properties.pop("style", "empty")

        def _duplicate(self, args):

            rv = super(LayeredImageMask, self)._duplicate(args)

            if self.mask:
                rv = AlphaMask(rv, self.mask)

            rv = Window(rv, style=self.style, **self.properties)

            return rv

    renpy.store.LayeredImageMask = LayeredImageMask

################################################################################
## Code to archive these files for a distributed game. Do not remove.
init python:
    build.classify("**alphamask_layeredimage.rpy", None)
    build.classify("**alphamask_layeredimage.rpyc", "archive")
################################################################################