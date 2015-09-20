#!/usr/bin/env python3

import sys
import re
import html
import bs4
from tkinter import *
from tkinter import ttk
import languages
import numberings



language = languages.english



class MainDialog(Tk):
    """Dialog window that lets the user set the options at the beginning of the plugin's run."""
    
    global parameters
    parameters = {}
        
    def __init__(self):
        
        super().__init__()
        self.title('Endnotes Adjuster')
        self.resizable(width=FALSE, height=FALSE)
        self.geometry('+100+100')
        self.mainframe = ttk.Frame(self, padding="12 12 12 12") # padding values's order: "W N E S"
        self.mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
        
        #label and listbox to select files to sound out for notes's list(s)
        self.labelInfo = ttk.Label(self.mainframe,
                                   text=language[0])
        self.labelInfo.grid(row=0, column=0, sticky=W, pady=5)
        
        self.scrollList = Scrollbar(self.mainframe, orient=VERTICAL)
        self.scrollXList = Scrollbar(self.mainframe, orient=HORIZONTAL)
        self.fileNameListbox = Listbox(self.mainframe, selectmode=EXTENDED,
                                       yscrollcommand=self.scrollList.set,
                                       xscrollcommand=self.scrollXList.set,
                                       exportselection=0)
        self.scrollList.grid(row=1, column=3, sticky=(N,E,S,W))
        self.scrollList['command'] = self.fileNameListbox.yview
        self.scrollXList.grid(row=2, column=0, columnspan=3, sticky=(W,S,E))
        self.scrollXList['command'] = self.fileNameListbox.xview
        
        self.fileNameListbox.grid(row=1, column=0, columnspan=3, sticky=(W,E))
        
        #checkbutton and combobox to select a class to refine the survey
        self.lookForAClass = BooleanVar()
        self.lookForAClassButton = ttk.Checkbutton(self.mainframe,
                                                   text=language[1],
                                                   variable=self.lookForAClass,
                                                   command=self.toggleDisabled,
                                                   state=NORMAL, onvalue=True,
                                                   offvalue=False)
        self.lookForAClassButton.grid(row=2, column=0, columnspan=3, pady=3, sticky=W)
        self.selectedClass = StringVar()
        self.selectClassCombobox = ttk.Combobox(self.mainframe,
                                                textvariable=self.selectedClass,
                                                state=DISABLED)
        self.selectClassCombobox.grid(row=3, column=0, columnspan=3, sticky=W)
        
        #label and radiobuttons to determine the behavior in front of an already existent id
        #of the note's reference in the text (options: overwrite, keep, ask everytime)
        ttk.Label(self.mainframe, text=language[2]).grid(row=4,
                                                               column=0,
                                                               columnspan=3, 
                                                               pady=5,
                                                               sticky=W)
        self.linkIdOverwrite = IntVar()
        ttk.Radiobutton(self.mainframe, 
                        text=language[3],
                        variable=self.linkIdOverwrite,
                        value=0).grid(row=5, column=0, sticky=W)
        ttk.Radiobutton(self.mainframe, 
                        text=language[4],
                        variable=self.linkIdOverwrite,
                        value=1).grid(row=6, column=0, sticky=W)
        ttk.Radiobutton(self.mainframe,
                        text=language[5],
                        variable=self.linkIdOverwrite,
                        value=2).grid(row=7, column=0, sticky=(N,W))
        
        ttk.Label(self.mainframe).grid(row=8, column=0)
        
        #checkbuttons to choose changes to do in stylesheets
        self.changeLiCss = BooleanVar()                                    
        changeLiCssCheckButton = ttk.Checkbutton(self.mainframe,
                        text=language[6],
                        variable=self.changeLiCss,
                        onvalue=True, offvalue=False)
        changeLiCssCheckButton.grid(row=9, column=0, columnspan=3, sticky=W)
        self.changeLiCss.set(True)
        
        self.changeOlCss = BooleanVar()
        changeOlCssCheckButton = ttk.Checkbutton(self.mainframe,
                        text=language[7],
                        variable=self.changeOlCss,
                        onvalue=True, offvalue=False)
        changeOlCssCheckButton.grid(row=10, column=0, columnspan=3, sticky=W)
        self.changeOlCss.set(True)
        
        ttk.Label(self.mainframe).grid(row=11, column=0)
        
        #label and combobox to choose the numbering for the notes
        ttk.Label(self.mainframe, text=language[26]).grid(row=12,
                                                          column=0,
                                                          columnspan=3,
                                                          sticky=W)
        self.selectedNumbering = StringVar()
        self.whichNumberingCombobox = ttk.Combobox(self.mainframe,
                                           textvariable=self.selectedNumbering,
                                           state='readonly')
        self.whichNumberingCombobox.grid(row=13, column=0, sticky=(W,E))
        
        ttk.Label(self.mainframe).grid(row=14, column=0)
        
        ttk.Button(self.mainframe, text=language[8],
                   command=self.saveParameters).grid(row=15, column=1, sticky=E)
        ttk.Button(self.mainframe, text=language[9],
                   command=self.quit).grid(row=15, column=2, sticky=E)
        
        
    def saveParameters(self):
        """Save global parameters and close dialog on OK button pressed"""
        noteIdFilesList = []
        for selectedId in self.fileNameListbox.curselection():
            noteIdFilesList.append(self.fileNameListbox.get(selectedId))
        parameters['idList'] = noteIdFilesList
        parameters['classtolookfor'] = self.selectedClass.get()
        parameters['overwrite'] = self.linkIdOverwrite.get()
        parameters['changelicss'] = self.changeLiCss.get()
        parameters['changeolcss'] = self.changeOlCss.get()
        parameters['numbering'] = self.selectedNumbering.get()
        self.destroy()
        
        
    def toggleDisabled(self):
        """Avoid the user to hurt herself fiddling with the combobox"""
        
        if self.lookForAClass.get() == True:
            self.selectClassCombobox.state(['!disabled', 'readonly'])
            self.selectedClass.set(self.olClassList[0])
        else:
            self.selectClassCombobox['state'] = DISABLED
            self.selectedClass.set('')
        
        
    def setListValues(self, bk):
        """Fill listbox and comboboxes with values"""
        
        counter = 0
        idLength = 0
        self.olClassList = []
        
        for fileId, fileHref in bk.text_iter():
            #Fill the listbox with file names
            self.fileNameListbox.insert(END, fileHref)
            counter +=1
            if len(fileHref) > idLength: 
                idLength = len(fileHref)
                
            #Find all the classes associated with tag "ol" in the epub
            classFinder = bk.readfile(fileId)
            classFinderBS = bs4.BeautifulSoup(classFinder, 'html.parser')
            for eachOl in classFinderBS.find_all('ol'):
                try:
                    for eachClass in eachOl.attrs['class']:
                        if eachClass not in self.olClassList:
                            self.olClassList.append(eachClass)
                except KeyError:
                    pass         
        self.selectClassCombobox.configure(values=self.olClassList)
        if not self.olClassList:
            self.lookForAClassButton['state'] = DISABLED
        
        #Set up the listbox
        if counter > 16: counter = 16
        else: self.scrollList.grid_remove()
        if idLength > 160: idLength = 160
        else: self.scrollXList.grid_remove()
        self.fileNameListbox['height'] = counter
        self.fileNameListbox['width'] = idLength + 2
        self.fileNameListbox.grid(row=1, column=0, columnspan=3, sticky=(W,E))
        
        #Choices of numbering
        numberingValues = ['1, 2, 3, 4...',
                           'A, B, C, D... (english alphabet)',
                           'a, b, c, d... (english alphabet)',
                           'A, B, C, D... (italian alphabet)',
                           'a, b, c, d... (italian alphabet)',
                           'I, II, III, IV...',
                           'i, ii, iii, iv...',
                           '01, 02, 03, 04...',
                           '001, 002, 003, 004...',
                           '0001, 0002, 0003, 0004...']
        self.whichNumberingCombobox.configure(values=numberingValues)
        self.selectedNumbering.set(numberingValues[0])
        
     
     
        
class IdDialog(Tk):
    """Dialog window that asks the user if she wants to keep or overwrite
    an already existent id on a note's reference in the text"""
    
    def __init__(self, aHref, aId, fileHref, counter):
        super().__init__()
        self.title(language[10])
        self.resizable(height=FALSE, width=FALSE)
        self.geometry('+350+200')
        self.mainframe = ttk.Frame(self, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
        self.labelInfo = ttk.Label(self.mainframe,
                                   text=language[11].format(
                                    fileHref, counter, aHref, aId),
                                   wraplength='430px')
        self.labelInfo.grid(row=0, column=0, columnspan=5, sticky=(N,W))
        self.buttonKeep = ttk.Button(self.mainframe, text=language[12], 
                                     command=lambda: self.keeporover(koo='keep'))
        self.buttonKeep.grid(row=1, column=1, sticky=(E,W))
        self.buttonOverwrite = ttk.Button(self.mainframe, text=language[13],
                                          command=lambda: self.keeporover(koo='overwrite'))
        self.buttonOverwrite.grid(row=1, column=2, sticky=(E,W))
        self.buttonKeepAll = ttk.Button(self.mainframe, text=language[14],
                                        command=lambda: self.keeporoverall(kooa=1))
        self.buttonKeepAll.grid(row=1, column=3, sticky=(E,W))
        self.buttonOverwriteAll = ttk.Button(self.mainframe, text=language[15],
                                             command=lambda: self.keeporoverall(kooa=0))
        self.buttonOverwriteAll.grid(row=1, column=4, sticky=(E,W))
    
    
    def keeporover(self, koo):    
        global keepOrOverwrite
        keepOrOverwrite = koo
        self.destroy()
        
        
    def keeporoverall(self, kooa):
        parameters['overwrite'] = kooa
        koo = 'overwrite' if kooa == 0 else 'keep'
        self.keeporover(koo)
        
   
        
         
def run(bk):
    
    #MainDialog lets the user set up the parameters
    form = MainDialog()
    form.setListValues(bk)
    form.mainloop()
    
    #At least one file must have been selected in order for the plugin to run
    try:
        assert parameters['idList']
    except (AssertionError, KeyError):
        print(language[16])
        return -1
    
    #to keep track of all the classes of the notes's "li" and "ol" tags 
    #and the id(s) of the "ol" tags
    liClassSet = set()
    olClassSet = set()
    olIdSet = set()
    
    #Begins the main loop of the plugin: every selected file will be 
    #searched for "ol" notes's container that will be replaced with "div".
    #Classes and id of the old container will be passed to the new.
    #If there isn't an id, will be inserted "NotesContainer_endNotesToParagraphPlugin"
    for idListItem in parameters['idList']:
        noteIdFile = bk.href_to_id(idListItem)
        noteFile = bk.readfile(noteIdFile)
        noteFileBS = bs4.BeautifulSoup(noteFile, 'html.parser')
        notesNewWrapper = noteFileBS.new_tag('div')
        notesOldWrapper = ''
        if parameters['classtolookfor']:
            for eachOl in noteFileBS.find_all('ol'):
                try:
                    for eachClass in eachOl['class']:
                        if eachClass == parameters['classtolookfor']:
                            notesOldWrapper = eachOl
                            break
                except KeyError:
                    pass
        else:
            notesOldWrapper = noteFileBS.ol
        if not notesOldWrapper:
            print(language[17].format(idListItem))
            continue
        try:
            notesNewWrapper['class'] = notesOldWrapper['class']
            for eachClass in notesOldWrapper['class']:
                olClassSet.add(eachClass)
        except KeyError:
            pass
        try:
            notesNewWrapper['id'] = notesOldWrapper['id']
            olIdSet.add(notesOldWrapper['id'])
        except KeyError:
            notesNewWrapper['id'] = 'NotesContainer_endNotesToParagraphPlugin'
        notesWrapper = notesOldWrapper.wrap(notesNewWrapper)
        notesOldWrapper.unwrap()
        print(language[18].format(noteIdFile))
        
        #Every first degree "li" tag in the notes's container will be replaced with "p".
        #It is necessary for the notes to already have an id, that will be used to look for
        #the references in the text (with the function refFinder, that also will add ids
        #to the references). Subsequently attribute href with the backlink will be added
        #to the notes.
        counter = 0
        for child in notesWrapper.children:
            if isinstance(child, bs4.element.Tag) and child.name == 'li':
                counter += 1
                attribs = child.attrs
                try:
                    for eachClass in attribs['class']:
                        liClassSet.add(eachClass)
                except KeyError:
                    pass
                childNewWrapper = noteFileBS.new_tag('p')
                childOldWrapper = child
                childWrapper = child.wrap(childNewWrapper)
                childOldWrapper.unwrap()
                print(language[19].format(counter))
                childWrapper.attrs = attribs
                idNote = childWrapper.a.attrs['id']
                backlinkRef = refFinder(noteIdFile, idNote, bk, counter)
                if backlinkRef:
                    childWrapper.a.attrs['href'] = backlinkRef[0]+'#'+backlinkRef[1]
                    print(language[20].format(counter))
                    orderSign = pickingNumbering(counter)
                    childWrapper.a.append('{}.'.format(orderSign))
                    childWrapper.a.insert_after(' ')
                    print(language[21].format(counter))
        bk.writefile(noteIdFile, decodeAdjuster(noteFileBS))
        
        #Modifying the css... 
        if parameters['changelicss']:
            changeCss(bk, liClassSet, 'li')
        if parameters['changeolcss']:
            changeCss(bk, olClassSet, 'ol_class')
            changeCss(bk, olIdSet, 'ol_id')
    return 0


def pickingNumbering(counter):
    if parameters['numbering'] == '1, 2, 3, 4...':
        return counter
    elif parameters['numbering'] == 'A, B, C, D... (english alphabet)':
        return numberings.intToString(counter, numberings.uppercase_letters)
    elif parameters['numbering'] == 'a, b, c, d... (english alphabet)':
        return numberings.intToString(counter, numberings.lowercase_letters)
    elif parameters['numbering'] == 'A, B, C, D... (italian alphabet)':
        return numberings.intToString(counter, numberings.italianize('upper'))
    elif parameters['numbering'] == 'a, b, c, d... (italian alphabet)':
        return numberings.intToString(counter, numberings.italianize('lower'))
    elif parameters['numbering'] == 'I, II, III, IV...':
        return numberings.intToRoman(counter, 'upper')
    elif parameters['numbering'] == 'i, ii, iii, iv...':
        return numberings.intToRoman(counter, 'lower')
    elif parameters['numbering'] == '01, 02, 03, 04...':
        return numberings.addZeroes(counter, 2)
    elif parameters['numbering'] == '001, 002, 003, 004...':
        return numberings.addZeroes(counter, 3)
    elif parameters['numbering'] == '0001, 0002, 0003, 0004...':
        return numberings.addZeroes(counter, 4)


#switcher should always assume values amongst 'li', 'ol_class' and 'ol_id'
def changeCss(bk, changerSet, switcher):
    """Regular expression are used to find and substitute li and ol 
    (associated with notes's classes and notes container's ids and classes)
    with p and div in the stylesheets"""
    
    if switcher == 'li':
        toChange = 'li'
        changeInto = 'p'
    else:
        toChange = 'ol'
        changeInto = 'div'
        
    for cssId, cssHref in bk.css_iter():
        numSubTot = 0
        cssLookup = ''
        cssSub = ''
        for element in changerSet:
            cssRead = bk.readfile(cssId)
            if switcher == 'ol_id':
                cssLookup += ''.join(('\n', toChange, '#', element))
                cssSub += ''.join(('\n', changeInto, '#', element))
                cssPattern = re.compile(toChange+r'(#{})'.format(element))
            else:
                cssLookup += ''.join(('\n', toChange, '.', element))
                cssSub += ''.join(('\n', changeInto, '.', element))
                cssPattern = re.compile(toChange+r'(\.{})'.format(element))
            cssRead, numSub = re.subn(cssPattern, changeInto+r'\1',
                                      cssRead.decode(), re.M)
            numSubTot += numSub
            bk.writefile(cssId, cssRead.encode())
        print(language[22].format(cssHref, cssLookup, 
                                  cssSub, numSubTot))


def refFinder(noteIdFile, idNote, bk, counter):
    """Look for notes's references in the epub (one for note),
    add an id to the reference if there isn't or, otherwise,
    overwrite/keep it (depending on user choice). Returns
    the complete reference to use for the backlink from the note"""
    
    for idFile, hrefFile in bk.text_iter():
#         if idFile == noteIdFile:
#             return
        fileRead = bk.readfile(idFile)
        fileReadBS = bs4.BeautifulSoup(fileRead, 'html.parser')
        for link in fileReadBS('a'):
            try:
                if link.attrs['href'].endswith(idNote):
                    try:
                        link.attrs['id']
                    except KeyError:
                        link.attrs['id'] = ''.join((idNote, 'backlink'))
                        bk.writefile(idFile, decodeAdjuster(fileReadBS))
                        print(language[23].format(counter, hrefFile))
                    else:
                        if parameters['overwrite'] == 0:
                            link.attrs['id'] = ''.join((idNote, 'backlink'))
                            bk.writefile(idFile, decodeAdjuster(fileReadBS))
                            print(language[23].format(counter, hrefFile))
                        elif parameters['overwrite'] == 1:
                            print(language[24].format(
                                    counter, hrefFile, idNote))
                        else:
                            form = IdDialog(link.attrs['href'],
                                            link.attrs['id'],
                                            hrefFile,
                                            counter)
                            form.mainloop()
                            if keepOrOverwrite == 'keep':
                                print(language[24].format(
                                        counter, hrefFile, idNote))
                            elif keepOrOverwrite == 'overwrite':
                                link.attrs['id'] = ''.join((idNote, 'backlink'))
                                bk.writefile(idFile, decodeAdjuster(fileReadBS))
                                print(language[23].format(counter, hrefFile))
                    finally:
                        backlink = link.attrs['id']
                        return (hrefFile, backlink)
            except KeyError:
                pass
    print(language[25].format(counter))
    
    
def decodeAdjuster(soup):
    """Replace html name entities with unicode characters.
    Exceptions: particular spaces, that would be lost, and xml entities"""
    soupDecoded = soup.decode(formatter='html')
    preserveEntities = {'&nbsp;':'&NBSP;',
                   '&ensp;':'&ENSP;',
                   '&emsp;':'&EMSP;',
                   '&thinsp;':'&THINSP;',
                   '&shy;':'&SHY;',
                   '&lt;':'&TL;', #these two are converted by html.unescape even if they are
                   '&gt;':'&TG;', #in uppercase or missing of the semicolon
                   '&quot;':'&QUOT;',
                   '&apos;':'&APOS;',
                   '&amp;': '&AMP;'}
    for x,y in preserveEntities.items():
        soupDecoded = soupDecoded.replace(x, y)
    soupDecoded = html.unescape(soupDecoded)
    for x,y in preserveEntities.items():
        soupDecoded = soupDecoded.replace(y, x)
    return soupDecoded
            
    
            
def main():
    print("I reached main when I should not have\n")
    return -1

if __name__ == '__main__':
    sys.exit(main())
