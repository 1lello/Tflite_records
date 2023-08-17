import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        print(f"Processing file: {xml_file}")  # Print the current XML file being processed
        
        filename = root.find('filename').text
        print(f"  Filename: {filename}")  # Print the filename
        
        width = int(root.find('size').find('width').text)
        height = int(root.find('size').find('height').text)
        print(f"  Width: {width}, Height: {height}")  # Print the width and height
        
        for member in root.findall('object'):
            class_name = member.find('name').text
            print(f"  Class Name: {class_name}")  # Print the class name
            
            xmin = int(member.find('bndbox').find('xmin').text)
            ymin = int(member.find('bndbox').find('ymin').text)
            xmax = int(member.find('bndbox').find('xmax').text)
            ymax = int(member.find('bndbox').find('ymax').text)
            print(f"  Bounding Box: {xmin}, {ymin}, {xmax}, {ymax}")  # Print the bounding box
            
            xml_list.append((filename, width, height, class_name, xmin, ymin, xmax, ymax))
            
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    
    return xml_df


