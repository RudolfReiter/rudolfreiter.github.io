from pybtex.database.input import bibtex

def get_personal_data():
    name = ["Rudolf", "Reiter"]
    email = "rudolf.reiter@imtek.uni-freiburg.de"
    bio_text = f"""
                <p>
                    I am currently pursuing a Ph.D. with the thesis title "Optimization-Based Motion Planning and Obstacle Avoidance for Autonomous Driving" under the supervision of Prof. Dr. Moritz Diehl and will defend in November 2024.

                    Since 2021, I have been part of a <a href="https://elo-x.eu/" target="_blank">Marie-Skłodowska Curie Innovative Training Network</a> for "embedded learning and optimization for the next generation of industrial systems". 
                    I hold a research position at the University of Freiburg, Germany, in the <a href="https://www.syscop.de/index.php/" target="_blank">Systems Control and Optimization Laboratory</a>. 
                    In the course of my doctoral research, I stayed at <a href="https://www.imtlucca.it/en" target="_blank">IMT Lucca</a> with Prof. Dr. Alberto Bemporad, at the <a href="https://www.merl.com/" target="_blank">Mitsubishi Electric Research Laboratories</a> in Cambridge, MA, US, and at <a href="https://idsc.ethz.ch/research-zeilinger.html" target="_blank">ETH Zürich</a> with Prof. Dr. Melanie Zeilinger to collaborate on research projects. 
                    <br>
                    Before starting my doctoral research, I studied electrical engineering at the <a href="https://www.tugraz.at/en/fakultaeten/etit/home" target="_blank">Graz University of Technology</a>, Austria, and worked in industry for several years.
                    In my Master's program, I focused on control systems and obtained the Master's degree in 2016. 
                    From 2016 to 2018, I worked as a control systems specialist at <a href=" https://www.anton-paar.com/corp-en/about-us/" target="_blank">Anton Paar GmbH</a> in Graz, Austria. 
                    From 2018 to 2021, I worked as a researcher for the <a href=" https://www.virtual-vehicle.at/" target="_blank">Virtual Vehicle Research Center</a> in Graz, Austria.  
                                          
                    My research focus is on learning- and optimization-based motion planning and control for autonomous robots, and I am an active member of the <a href="https://autonomousracing.ai/" target="_blank">Autonomous Racing Graz</a> team.
                </p>
                
                <p>
                    <a href="https://rudolfreiter.github.io/assets/pdf/reiter_cv2.pdf" target="_blank" style="margin-right: 15px"><i class="fa fa-address-card fa-lg"></i> CV</a>
                    <a href="mailto:{email}" style="margin-right: 15px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://scholar.google.com/citations?user=5VdYugYAAAAJ&hl=en" target="_blank" style="margin-right: 15px"><i class="fa-solid fa-book"></i> Scholar</a>
                    <a href="https://github.com/RudolfReiter" target="_blank" style="margin-right: 15px"><i class="fab fa-github fa-lg"></i> Github</a>
                    <a href="https://www.linkedin.com/in/rudolf-reiter-ba8777157" target="_blank" style="margin-right: 15px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                </p>

            <!--
                <p>
                    <a href="https://m-niemeyer.github.io/assets/other/bio.txt" target="_blank" style="margin-right: 5px"><i class="fa-solid fa-graduation-cap"></i> Bio</a>
                    <a href="https://m-niemeyer.github.io/assets/pdf/CV_Niemeyer_Michael.pdf" target="_blank" style="margin-right: 5px"><i class="fa fa-address-card fa-lg"></i> CV</a>
                    <a href="mailto:micniemeyer1@gmail.com" style="margin-right: 5px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://twitter.com/Mi_Niemeyer" target="_blank" style="margin-right: 5px"><i class="fab fa-twitter fa-lg"></i> Twitter</a>
                    <a href="https://scholar.google.com/citations?user=v1O7i_0AAAAJ&hl=en" target="_blank" style="margin-right: 5px"><i class="fa-solid fa-book"></i> Scholar</a>
                    <a href="https://github.com/m-niemeyer" target="_blank" style="margin-right: 5px"><i class="fab fa-github fa-lg"></i> Github</a>
                    <a href="https://www.linkedin.com/in/michael-niemeyer" target="_blank" style="margin-right: 5px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                    <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#demo" data-toggle="collapse" style="margin-left: -6px; margin-top: -2px;"><i class="fa-solid fa-trophy"></i>Awards</button>
                    <div id="demo" class="collapse">
                    <span style="font-weight: bold;">Awards:</span>
                    In 2011, I graduated as top of my year from secondary school and received <a href="https://www.e-fellows.net/" target="_blank">the e-fellows scholarship</a> and was admitted to <a href="https://www.mathematik.de/" target="_blank">the Germany Mathematics Society</a> and <a href="https://www.dpg-physik.de/" target="_blank">the German Physics Society</a>. In 2017 I received the Dean's List Award for Academic Excellence for my Master's degree.
                    During my PhD studies, I was a scholar of <a href="https://imprs.is.mpg.de/" target="_blank">the International Max Planck Research School for Intelligent Systems (IMPRS-IS)</a>.
                    Our research projects Occupancy Networks, DVR, and ConvOnet were selected to be among the 15 most influencial <a href="https://www.paperdigest.org/2021/03/most-influential-cvpr-papers-2021-03/" target="_blank">CVPR</a> /  <a href="https://www.paperdigest.org/2023/09/most-influential-eccv-papers-2023-09/" target="_blank">ECCV</a> papers of 2019 and 2020.
                    In 2021, we received the CS teaching award for our <a href="https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/autonomous-vision/lectures/computer-vision/" target="_blank">computer vision lecture</a> as well as  <a href="https://cyber-valley.de/en/news/meet-the-ai-gamedev-winners" target="blank">the AIGameDev scientific award</a> for our GRAF project and <a href="https://cvpr2021.thecvf.com/node/329" target="_blank">the CVPR Best Paper Award</a> for GIRAFFE (<a href="https://cyber-valley.de/en/news/best-paper-cvpr-2021" target="_blank">news coverage</a>).
                </div>
                </p>
            -->
    """
    footer = """
            <div class="col-sm-12" style="">
                <h4>Homepage Template</h4>
                <p>
                   This homepage is based on a <a href="https://github.com/m-niemeyer/m-niemeyer.github.io" target="_blank">template of Michael Niemeyer</a>. <br>
                </p>
            </div>
    """
    return name, bio_text, footer

def get_author_dict():
    return {
        }

def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name='Michael Niemeyer', add_links=True):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        string_part_i = ""
        for name_part_i in p.get_part('first') + p.get_part('last'): 
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        if string_part_i in links.keys():
            string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s

def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    if 'award' in entry.fields.keys():
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'html': 'Project Page', 'pdf': 'Paper', 'supp': 'Supplemental', 'video': 'Video', 'poster': 'Poster', 'code': 'Code'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')

    cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}" + "}, \n"
    for entr in ['title', 'booktitle', 'year']:
        cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""
    s += " /" + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """ </div> </div> </div>"""
    return s

def get_talk_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'slides': 'Slides', 'video': 'Recording'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    s += """ </div> </div> </div>"""
    return s

def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_paper_entry(k, bib_data.entries[k])
    return s

def get_talks_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('talk_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_talk_entry(k, bib_data.entries[k])
    return s

def get_index_html():
    pub = get_publications_html()
    talks = get_talks_html()
    name, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <title>{name[0] + ' ' + name[1]}</title>
  <link rel="icon" type="image/x-icon" href="assets/favicon.ico">
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-10">
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="margin-bottom: 1em;">
                    <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
                    </div>
                    <br>
                    <div class="col-md-9" style="">
                        {bio_text}
                    </div>
                    <div class="col-md-3" style="">
                        <img src="assets/img/profile.png" class="img-thumbnail" height="680px" alt="Profile picture">
                    </div>
                </div>
                <div class="row" style="margin-top: 1em;">
                    <div class="col-sm-12" style="">
                        <h4>Publications</h4>
                        {pub}
                    </div>
                </div>
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="">
                        <h4>Talks</h4>
                        {talks}
                    </div>
                </div>
                <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
                    {footer}
                </div>
            </div>
            <div class="col-md-1"></div>
        </div?
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w') as f:
        f.write(s)
    print(f'Written index content to {filename}.')

if __name__ == '__main__':
    write_index_html('index.html')
