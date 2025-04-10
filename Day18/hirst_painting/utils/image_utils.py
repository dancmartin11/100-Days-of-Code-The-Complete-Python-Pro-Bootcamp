#Import libraries
import colorgram

#Utilities for modifying and accessing image attributes
class Image():
    '''
    Image object, should be any image file (e.g. .JPG, .PNG)
    
    Args:
        image_path (str): Path to the image whose colors will be extracted.
    '''
    def __init__(self, image_path: str):
        self.image_path = image_path

    def extract_colors(self, n_colors: int) -> list:
        '''
        Function that extracts the RGB for a selected number of colors from an input image.

        Args:
            n_colors (int): Number of colors that will be extracted, each color will be an RGB tuple in the output list.
            
        Returns:
            list: List of tuples that represent the RGB of each color.
        '''
        
        #Extract color palette from selected image
        extracted_colors = colorgram.extract(self.image_path, n_colors)

        #Iterate in the color objects to extract RGB values in tuples, then store all color tuples in list
        colors_list = []

        for i in range(len(extracted_colors)):
            #Get each single color object
            color = extracted_colors[i]
            #Empty list to store RGB for each color
            rgb = []
            #Generate color tuple extracting from rgb attribute of color object
            for x in color.rgb:
                rgb.append(x)
            rgb = tuple(rgb)
            #After RGB tuple is generated, append color to color list
            colors_list.append(rgb)
            
        return colors_list