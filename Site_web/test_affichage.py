# coding: utf-8
import cvs_to_web as cw;
import os;
def index():
    titre = "Titre"
    m = deb(titre)
    m += header()
    m += liens()
    m += home()
    m += research()
    m += bio()
    folder = '/Users/stephane/Documents/git/Site_web/Site_web/'
    file_intership = folder+'database/internships.csv'
    file_collaborators = folder+'database/collaborators.csv'
    m += people(file_intership, file_collaborators)
    file_article = folder+'database/mesarticles.bib'
    m += publi(file_article)
    m += contact()
    m += fin()
    return m

def deb(titre):
    message = """
    <html>
    <head>
        <title>
    """
    message+=titre
    m = """
        </title>
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="css/index.css">
    </head>
    <body>
    """
    message+=m
    return message

def header():
    message = """
        <header>
            <div id="header">
                <img src="image/portrait_SPerrard.png">
                <section id="titre">
                    <h1>Nom </h1>
                    <h2><i>Titre</i></h2>
                    <h2>Titre</h2>
                </section>
            </div>
        </header>
    """
    return message

def liens():
    message = """
        <section id="menu">
            <section id="flexmenu">
                <ul id="bouton">
                    <li><button type="button" onclick="allerA('research')">Research</button></li>
                    <li><button type="button" onclick="allerA('bio')">Bio</button></li>
                    <li><button type="button" onclick="allerA('people')">People</button></li>
                    <li><button type="button" onclick="allerA('publi')">Publication</button></li>
                    <li><button type="button" onclick="allerA('contact')">Contact</button></li>
                </ul>
            </section>
        </section>
    """
    return message

def home():
    message = """
        <section id="home" class="hide">
            <h3>Home</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ex justo, volutpat at scelerisque in, vulputate non neque. Proin pharetra accumsan mauris, vitae ornare purus viverra elementum. Aenean ante nunc, finibus vel purus non, egestas laoreet mi. In feugiat porttitor luctus. Aliquam ac maximus lectus. Donec mi nibh, iaculis nec risus non, rhoncus ultrices nibh. In pulvinar scelerisque nibh quis consectetur. Cras fermentum, magna at dignissim malesuada, augue leoullamcorper turpis, eu aliquet metus est ac enim. In ipsum massa, eleifend quis porta non, rhoncus id tellus. Mauris sit amet magna viverra, fringilla purus quis, vehicula ligula. Pellentesque efficitur, nisl in commodo placerat, nisi elit viverra metus, ut volutpat turpis leo dictum tortor. Donec finibus elit nisl, id interdum lorem dictum at. </p>
            <p> Quisque convallis nisl lectus. Donec varius lacus a libero mattis, a tincidunt ligula sagittis. Fusce dui risus, laoreet nec erat vitae, blandit luctus erat. Vestibulum cursus accumsan odio, nec suscipit quam facilisis nec. Donec egestas mollis mi, sed condimentum ex rutrum a. Pellentesque neque diam, semper ac nulla ac, lobortis aliquet lorem. Suspendisse potenti. Morbi sollicitudin lacinia ultrices. Cras magna lectus, consequat vitae ex eget, hendrerit fermentum erat. Duis feugiat, quam vel aliquam elementum, dolor lectus iaculis magna, et faucibus arcu turpis a ligula. Etiam non convallis neque, efficitur maximus odio. Ut leo metus, interdum ac varius vitae, imperdiet ut purus. </p>
        </section>
    """
    return message

def research():
    message = """
        <section id="research" class="sshow">
            <p> I am an experimental Physicist with a strong interest for non linear dynamics and multi-scale systems. I often combine experiments, theory and toy model numerical simulations. My research area includes surface waves, hydrodynamic turbulence, dynamical systems and statistical physics. </p>
            <button id="retour" class="hide" onclick="liste()">Retour</button>
            <div id="flexr">
                <span class="show bubble_breaking">
                    <a onclick="cacher('bubble_breaking')">
                        <h4>Turbulence & Interfaces</h4>
                        <img src="image/ballooncloseup.png" />
                    </a>
                </span>
                <span class="show pilot_wave">
                    <a onclick="cacher('pilot_wave')">
                        <h4>Memory-driven systems</h4>
                        <img src="image/walker.png" />
                    </a>
                </span>
                <span class="show surface_wave">
                    <a onclick="cacher('surface_wave')">
                        <h4>Waves & Capillarity </h4>
                        <img src="image/Torus.png" />
                    </a>
                </span>
                <span class="show hydro_turbulence">
                    <a onclick="cacher('hydro_turbulence')">
                        <h4>Large scale dynamics</h4>
                        <img src="image/Large_scale.png" />
                    </a>
                </span>

                <span class="show wind_wave">
                    <a onclick="cacher('wind_wave')">
                        <h4>Wind waves</h4>  </br> </br>
                        <img src="image/WrinklesFourier.png" />
                    </a>
                </span> 
            </div>"""
    message += article1()
    message += article2()
    message += article3()
    message += article4()
    message += article5()
    message +="""
        </section>
    """
    return message

def article1():
    message = """
            <div class="article hide wind_wave">
                <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec porta, ligula vel dignissim maximus, felis neque maximus leo, non interdum ipsum neque et tellus. Aliquam non libero mollis, dapibus tellus ac, tempus risus. Pellentesque ac interdum neque. Mauris tristique lacus lacus, interdum suscipit nisi rhoncus vel. Aenean volutpat nisl eget malesuada tincidunt. Fusce eget erat odio. Aliquam at egestas augue. Nulla libero ex, vehicula nec suscipit in, dignissim in urna. Fusce feugiat imperdiet arcu, a suscipit magna sollicitudin vitae. Fusce sit amet metus augue. Etiam nec volutpat enim. Praesent sed nulla commodo, tincidunt ante non, sagittis felis. Quisque sit amet velit placerat leo tempor tempor aliquet et justo. </p>
            </div>
    """
    return message
def article2():
    message = """
            <div class="article hide bubble_breaking">
                <p>Nullam non ullamcorper ex. Fusce non ornare justo, ac condimentum sapien. Phasellus mauris ligula, pharetra in est nec, pretium interdum leo. Nullam non orci porttitor, finibus nisi quis, tempor tellus. Proin pulvinar diam vitae tempus sodales. Proin vitae enim tortor. Suspendisse in sem justo. Nullam et semper odio. Nam finibus placerat lorem, eu sollicitudin diam feugiat et. Vivamus sem eros, dignissim ac odio et, euismod eleifend tellus. </p>
            </div>
    """
    return message
def article3():
    message = """
            <div class="article hide hydro_turbulence">
                <p>Vestibulum vel auctor sem. Nullam tincidunt cursus tincidunt. Aenean imperdiet eros est, at tincidunt velit lacinia imperdiet. In lacinia purus non enim condimentum eleifend. Ut et efficitur erat, a pellentesque risus. Curabitur imperdiet dapibus enim, a tincidunt turpis convallis ac. Nulla a ornare lacus. Donec eleifend massa id mattis rhoncus. Cras consequat eget est quis consequat. Suspendisse a venenatis est. </p>
            </div>
    """
    return message
def article4():
    message = """
            <div class="article hide pilot_wave">
                <p>Nulla vestibulum nunc sed mauris maximus, non imperdiet neque volutpat. Integer gravida convallis porta. Duis posuere turpis faucibus metus fringilla consectetur. Quisque maximus lorem vel mauris tempor egestas. Quisque in erat eget elit varius dictum. Quisque in leo lacus. Morbi ultrices, mauris vel consequat eleifend, felis lectus vulputate quam, sagittis posuere risus turpis eget risus. Vestibulum feugiat nibh nec consequat blandit. Nulla orci nisl, maximus sit amet erat ut, accumsan euismod nulla. </p>
            </div>
    """
    return message
def article5():
    message = """
            <div class="article hide surface_wave">
                <p>Donec sit amet lacinia justo. Aliquam dignissim nibh arcu, nec pulvinar risus lacinia vel. Aliquam quis faucibus felis, sed ullamcorper augue. Donec hendrerit lorem ut dignissim faucibus. Ut in nunc eros. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut a elementum sapien, ut semper massa. Nullam imperdiet sodales congue. Maecenas rutrum sem eu nulla tristique gravida. Integer sed posuere ante, non tincidunt sem. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Quisque aliquam est ante, ac accumsan massa lacinia eu. </p>
            </div>
    """
    return message

def bio():
    message = """
        <section id="bio" class="hide">
            <h3>Bio</h3>
        </section>
    """
    return message

def people(file_intership, file_collaborators):
    message = """
        <section id="people" class="hide">
            <h3>People</h3>
            <h4>Present & past collaborators </h4>
            <p>"""
    t=cw.contributor(file_collaborators)
    message +=str(t)
    message +="""</p>
            <h4>Past supervised students</h4>
            <p>"""
    t=cw.internship(file_intership)
    message +=str(t)
    message +="""</p>
        </section>
    """
    return message

def publi(file_article):
    message = """
        <section id="publi" class="hide">
            <h3>Publication</h3>
    """
    message +=cw.article(file_article)
    message +="""
        </section>
    """
    return message

def contact():
    message = """
        <section id="contact" class="hide">
            <h3>Contact</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ex justo, volutpat at scelerisque in, vulputate non neque. Proin pharetra accumsan mauris, vitae ornare purus viverra elementum. Aenean ante nunc, finibus vel purus non, egestas laoreet mi. In feugiat porttitor luctus. Aliquam ac maximus lectus. Donec mi nibh, iaculis nec risus non, rhoncus ultrices nibh. In pulvinar scelerisque nibh quis consectetur. Cras fermentum, magna at dignissim malesuada, augue leoullamcorper turpis, eu aliquet metus est ac enim. In ipsum massa, eleifend quis porta non, rhoncus id tellus. Mauris sit amet magna viverra, fringilla purus quis, vehicula ligula. Pellentesque efficitur, nisl in commodo placerat, nisi elit viverra metus, ut volutpat turpis leo dictum tortor. Donec finibus elit nisl, id interdum lorem dictum at. </p>
        </section>
    """
    return message

def fin():
    message = """
        <script type="text/javascript" src="JS/suivant.js"></script>
    </body>
    </html>
    """
    return message
