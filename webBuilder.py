#Ash Lewis
#Web Builder
from tkinter import *
import math

#Blank Window
#root = Tk()

#Array Declarations
link = []
background = []

#---Function Declarations----------------------------------------------------------------------------------------------------------------------------------

def openCSS(fileCSS):
    open = 'body{\n'
    fileCSS.write(open)

#Tool bar maker
def makeTool():
    
    print("This is where you will make your tool bar.")
    
    linkAmt = int(input("How many links do you want ?"))
    
    for x in range (0, linkAmt):
        linkTitle = str(input("What do you want this page to be called ?"))
        link.append(linkTitle)
             
      
#Color theme for the website   
def makeTheme(fileCSS):
    
    bakCol = int(input("What color do you want your background ? 1 for black\n 2 for white\n 3 for red\n 4 for orange\n 5 for yellow \n 6 for green\n 7 for blue\n 8 for purple")) #Background Color of the article

    if (bakCol == 1):
        backColor = '#000000'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')

    elif (bakCol == 2):
        backColor = '#FFF'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')

    elif (bakCol == 3):
        backColor = '#FF0000'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')

    elif (bakCol == 4):
        backColor = '#FFA500'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')
        
    elif (bakCol == 5):
        backColor = '	#FFFF00'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')
    
    elif (bakCol == 6):
        backColor = '#76EE00'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')
    
    elif (bakCol == 7):
        backColor = '#104E8B'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')
    
    else:
        backColor = '#7D26CD'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')


    #Text color
    txtCol = int(input("What color do you want your text ? 1 for black\n 2 for white\n 3 for red\n 4 for orange\n 5 for yellow \n 6 for green\n 7 for blue\n 8 for purple")) #Background Color of the article

    if (txtCol == 1):
        textColor = '#000000'
        fileCSS.write('\ncolor: ' + textColor +';\n')

    elif (txtCol == 2):
        textColor = '#FFF'
        fileCSS.write('\ncolor: ' + textColor +';\n')

    elif (txtCol == 3):
        textColor = '#FF0000'
        fileCSS.write('\ncolor: ' + textColor +';\n')

    elif (txtCol == 4):
        textColor = '#FFA500'
        fileCSS.write('\ncolor: ' + textColor +';\n')
        
    elif (txtCol == 5):
        textColor = '	#FFFF00'
        fileCSS.write('\ncolor: ' + textColor +';\n')
    
    elif (txtCol == 6):
        textColor = '#76EE00'
        fileCSS.write('\ncolor: ' + textColor +';\n')
    
    elif (txtCol == 7):
        textColor = '#104E8B'
        fileCSS.write('\ncolor: ' + textColor +';\n')
    
    else:
        textColor = '#7D26CD'
        fileCSS.write('\ncolor: ' + textColor +';\n')
        
    fileCSS.write('}\n\n')        
#Title
def getTitle():
    
    title = str(input("What is the title of your site ?"))
    
    return title
    
#Image
def getImage():
    
    pic = int(input("Do you want an image for your site ? 1 for yes, and 2 for no")) #If user wants a picture on their article
    
    return pic

#Format page
def getFormat():
    
        format = int(input("Select a layout for your website. 1 for blog, 2 for portfolio, 3 for grid")) #What layout does the user want
        
        return format;
        
#Insert Form      
def getForm():
    
    format = int(input("Select a layout for your website. 1 for blog, 2 for portfolio, 3 for grid")) #What layout does the user want

#Header
def getHeader():
    
    head = str(input("Write a heading")) #User writes a article heading
    
    return head
    
#Article
def makeArticle():
    
    par = str(input("Write your article")) #The article content
    
    return par
 
#Making the link tab
def writeTop(title, fileHTML, fileCSS):
    
    fileCSS.write('.containter\n{\nwidth: 80%;\nmargin: 0 auto;\n}\n\nheader\n{\n')
    
    bakCol = int(input("What color do you want your header background ? 1 for black\n 2 for white\n 3 for red\n 4 for orange\n 5 for yellow \n 6 for green\n 7 for blue\n 8 for purple")) #Background Color of the article



    if (bakCol == 1):
        backColor = '#000000'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')

    elif (bakCol == 2):
        backColor = '#FFF'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')

    elif (bakCol == 3):
        backColor = '#FF0000'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')

    elif (bakCol == 4):
        backColor = '#FFA500'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')
        
    elif (bakCol == 5):
        backColor = '	#FFFF00'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')
    
    elif (bakCol == 6):
        backColor = '#76EE00'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')
    
    elif (bakCol == 7):
        backColor = '#104E8B'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')
    
    else:
        backColor = '#7D26CD'
        fileCSS.write('\nbackground-color: ' + backColor +';\n')

    fileCSS.write('height: 10%;\n}\nheader nav ul li {\ndisplay: inline;\npadding:2%;\n}\nheader nav ul li a{\nfont-weight: bold;\nfont-size: 35px;\n\n')
    
    #Text color
    txtCol = int(input("What color do you want your text ? 1 for black\n 2 for white\n 3 for red\n 4 for orange\n 5 for yellow \n 6 for green\n 7 for blue\n 8 for purple")) #Background Color of the article

    if (txtCol == 1):
        textColor = '#000000'
        fileCSS.write('\ncolor: ' + textColor +';\n')

    elif (txtCol == 2):
        textColor = '#FFF'
        fileCSS.write('\ncolor: ' + textColor +';\n')

    elif (txtCol == 3):
        textColor = '#FF0000'
        fileCSS.write('\ncolor: ' + textColor +';\n')

    elif (txtCol == 4):
        textColor = '#FFA500'
        fileCSS.write('\ncolor: ' + textColor +';\n')
        
    elif (txtCol == 5):
        textColor = '	#FFFF00'
        fileCSS.write('\ncolor: ' + textColor +';\n')
    
    elif (txtCol == 6):
        textColor = '#76EE00'
        fileCSS.write('\ncolor: ' + textColor +';\n')
    
    elif (txtCol == 7):
        textColor = '#104E8B'
        fileCSS.write('\ncolor: ' + textColor +';\n')
    
    else:
        textColor = '#7D26CD'
        fileCSS.write('\ncolor: ' + textColor +';\n')
        
    fileCSS.write('\n}\nheader nav ul li a:hover {\n color: white;\n}\n')        
    
    open = '<html>\n\n<head>' + title +  '\n<link href = "webStyle.css" rel = "stylesheet" type = "text/css">\n</head>\n\n<body>\n\n<header>\n<div class="container">\n<h3 class="logo">' + title + '</h3>\n<nav>\n<ul style="display:inline, padding: 4%">\n'  #<link href = "webStyle.css" rel = "stylesheet" type = "text/css">
    
    fileHTML.write(open)
    
    for x in range (0, len(link)):
        
        insert = '<li><a href="index' + str(x) + '.html" > ' + link[x] + ' </a></li>\n'
        fileHTML.write(insert)
        
    close = '</ul>\n</nav>\n</div>\n</header>\n\n'
    fileHTML.write(close)
    
#def writeMid():    

def closeHTML(fileHTML):
    
    close = '\n\n</body>\n\n</html>\n'
    fileHTML.write(close)    


#Where the user will insert content to the layout
def getEntry(fileHTML):
    
    fileHTML.write('\n<section class="display">\n\n')
    
    entries = int(input("Type how many entries you want in the page"))
    
    for x in range (0, entries):
        
        fileHTML.write('<div class="display' + str(x) + '">')
        
        #If user wants image for the block    
        picChoice = int(input("do you want an image ?"))
        
        if(picChoice == 1):
            
            addChoice = int(input("Do you want to upload an image, or past a url ?"))
            
            if(addChoice == 1):
                print("You choose to upload")
                
            if(addChoice == 2):
                picURL = str(input("Paste your URL here: "))
                fileHTML.write('<img src="' + picURL + '"></img>')                
                
        
        #If user wants a header for the block
        headerChoice = int(input("Do you want a header ?"))
        
        if(headerChoice == 1):
            
            addChoice = int(input("Is this a link ?"))
            
            if(addChoice == 1):
                
                header = str(input("Write the header: "))
                
                fileHTML.write('<a href ="#"><h1>' + header + '</h1></a>')
            
            if(addChoice == 2):
                
                header = str(input("Write the header: "))
                               
                fileHTML.write('<h1>' + header + '</h1>')               
                       
         #What the user will write in the block 
        pChoice = int(input("Do you want to write a caption ?"))
        
        if(pChoice == 1):
            
            article = str(input("Write content here."))
            
        fileHTML.write('\n</div>\n\n')            
            
    fileHTML.write('\n</section>\n')  
    


#--Function Calls---------------------------------------------------------------------------------------------------------------------------------------------
fileHTML = open('c:/test/index.html','w') #HTML open
fileCSS = open('c:/test/webStyle.css', 'w') #CSS open
title = getTitle()
openCSS(fileCSS)
theme = makeTheme(fileCSS)
tool = makeTool()
writeTop(title, fileHTML, fileCSS)
format = getFormat()
pic = getImage()
entry = getEntry(fileHTML)
header = getHeader()
article = makeArticle()
closeHTML(fileHTML)
fileHTML.close() #HTML close
fileCSS.close() #CSS close