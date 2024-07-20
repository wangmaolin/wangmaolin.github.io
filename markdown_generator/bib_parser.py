from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

def main():
    parser = bibtex.Parser()
    bibdata = parser.parse_file('./new-paper.bib')
    for bib_idx in bibdata.entries:
        item_fields = bibdata.entries[bib_idx].fields
        # print(item_fields['Booktitle'])

        pub_year = f'{item_fields["year"]}'
        # clean_title = item_fields["title"].replace("{", "").replace("}","").replace("\\","").replace(" ","-")    
        clean_title = item_fields["title"].replace("{", "").replace("}","").replace("\\","")    

        md_contents = "---\ntitle: \""   + html_escape(item_fields["title"].replace("{", "").replace("}","").replace("\\","")) + '"\n'
        md_filename = (pub_year+"-"+bib_idx + ".md")
            
        md_contents += """collection: publications"""
        md_contents += """\npermalink: /publication/""" 
        # md_contents += "\nvenue: '" + html_escape(venue) + "'"
        md_contents += "\n---\n"
 
        citation = ""
        """ Authors """
        all_authors= bibdata.entries[bib_idx].persons['Author']
        for author_idx, author_item in enumerate(all_authors):
            if author_idx == len(all_authors) - 1:
                citation += "and "  
            if author_item.first_names[0] == "Maolin":
                citation += "**"+author_item.first_names[0]+" "+author_item.last_names[0]+"**, "
            else:
                citation += author_item.first_names[0]+" "+author_item.last_names[0]+", "

        citation += "\""
        citation += clean_title
        citation += "\", in *"
        if 'Booktitle' in item_fields:
            citation += item_fields['Booktitle']
        else:
            citation += item_fields['journal']
        citation += "*, "
        citation += item_fields['Year']
        citation += "\n"
        
        md_contents += citation

        """ write to publications """
        print(md_contents)
        with open("../_publications/" + md_filename, 'w') as f:
            f.write(md_contents)
        # break

if __name__ == '__main__':
    main()