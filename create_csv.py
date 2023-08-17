import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Read the filename from the 'filename' tag
        filename = root.find('filename').text
        
        # Read the image width and height from the 'size' tag
        width = int(root.find('size').find('width').text)
        height = int(root.find('size').find('height').text)
        
        # Iterate over each 'object' tag in the XML
        for member in root.findall('object'):
            # Read the class name from the 'name' tag within the 'object' tag
            class_name = member.find('name').text
            
            # Read the bounding box coordinates from the 'bndbox' tag within the 'object' tag
            xmin = int(member.find('bndbox').find('xmin').text)
            ymin = int(member.find('bndbox').find('ymin').text)
            xmax = int(member.find('bndbox').find('xmax').text)
            ymax = int(member.find('bndbox').find('ymax').text)
            
            # Append the extracted information as a tuple to the xml_list
            xml_list.append((filename, width, height, class_name, xmin, ymin, xmax, ymax))
    
    # Create a DataFrame from the xml_list
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    
    return xml_df

def main():
    for folder in ['train','validation']:
        image_path = os.path.join(os.getcwd(), ('images/' + folder))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv(('images/' + folder + '_labels.csv'), index=None)
        print('Successfully converted xml to csv.')

main()

