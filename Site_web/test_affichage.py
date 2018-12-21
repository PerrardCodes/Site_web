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
            <button id="retour" class="hide" onclick="liste()">Retour</button>
            <div id="flexr">
                <span class="show bubble_breaking">
                    <a onclick="cacher('bubble_breaking')">
                        <h4>Turbulence & Interfaces</h4>
                        <img src="image/ballooncloseup.png" />
                    </a>
                </span>
                
                <span class="show wind_wave">
                    <a onclick="cacher('wind_wave')">
                        <h4>Wind waves</h4>  </br> </br>
                        <img src="image/WrinklesFourier.png" />
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
    
            <div class="article hide bubble_breaking">
            <div class=flex_article>
               <p>
               The breaking of an air bubble in a turbulent flow generally occurs above a critical bubble size called the Hinze scale, 
               at which surface tension and inertial forces balance. What happens if a much large bubble than the Hinze scale is created? 
               We investigate this highly non linear configuration by cracking air balloons in a jet generated turbulent background flow. 
               This work is done in collaboration with Pr L. Deike (Princeton University, Mechanical & Aerospace Engineering).
               </p>
               <img src="image/ballonbreaking.png" />
            </div>
            </div>
    """
    return message
    
def article2():
    message = """
            <div class="article hide pilot_wave">
                        <div class=flex_article>

                <p>
                Over the past 15 years, oil drops bouncing on a vibrated liquid bath have drawn growing attention as a rare example 
                of macroscopic wave-particle duality. Following my PhD work, we investigate numerically the general behavior of memory driven systems
                in disordered phases. We study in particular the emerging statistical behaviour reminiscent of the wave guiding field. 
                Most recent works have been done in collaboration with M. Labousse (ESPCI, Laboratoire Gulliver) and M. Hubert (Université de Liège, GRASP). 
                </p>
                <img src="image/walkers.png" />

            </div>
            </div>
    """
    return message
def article3():
    
    message = """
            <div class="article hide wind_wave">
                        <div class=flex_article>

                <p>
                When the wind blows over the ocean, it generates surface waves. The current theories can be traced back to the 50s’ [1,2], 
                but the underlying mechanism are not yet fully understood. Following a recent experimental advance of Paquier et al. [3], 
                we recently showed that the structures generated by the wind below the wind threshold are reminiscent of air pressure fluctuations.
                The link between the reminiscent structures called wrinkles and the wind threshold is still to investigate. 
                This work is done in collaboration with F. Moisy & M. Rabaud (Université Paris-Sud, FAST) and M. Benzaquen (Ecole Polytechnique, LadHyX)
                </p>
                
                <img src="image/numerical_setup.png" />

            </div>
            </div>
            """
    return message
    
def article4():
    message = """
            <div class="article hide hydro_turbulence">
                        <div class=flex_article>

                <p> 
                In hydrodynamic Turbulence, tremendous research efforts have been devoted to the study of Navier-Stokes equation with
                a finite energy transfer rate from an integral length scale toward small scales as pictured in Fourier space (see image). 
                Less is known on the dynamics of the large scale structures, i.e. that larger than the integral length scale. 
                We aim at designing lab experiments to observe and study the dynamics of these large scales. 
                This work is done in collaboration with S. Fauve & F. Pétrélis (ENS Paris, LPS) and M. Berhanu & E. Falcon (University Paris-Diderot, Paris)
                </p>
                
                <img src="image/Large_scale_turbulence.png" />


                </div>
                </div>
            """
    return message
    
def article5():
    message = """
            <div class="article hide surface_wave">
                        <div class=flex_article>

                <p>When a liquid drop is poured onto a very hot surface, it can levitate on its own vapor film. 
                The so-called Leidenfrost effect is a graal for the experimental physicist as a tool to isolate liquids from any solid contact. 
                Using curved heated substrate, we achieve levitation of liquid cylinder of macroscopic sizes, typically 50cm long and 1cm wide. 
                This experimental discovery led to the study of surface waves on exotic geometries (toroidal channel, linear channel, symetric and asymetric channels). 
                Current works are done in collaboration with C.T. Pham (Université Paris-Sud, LIMSI).
                </p>       
                
                <img src="image/Levitated_liquids.png" />
         
                </div>
                </div>
    """
    return message

def bio():
    message = """
        <section id="bio" class="hide">
            <p> I am an experimental Physicist with a strong interest for non linear dynamics and multi-scale systems. 
            I often combine experiments, theory and toy model numerical simulations.
            My research area includes surface waves, hydrodynamic turbulence, dynamical systems and statistical physics. </p>
        </section>
    """
    return message

def people(file_intership, file_collaborators):
    message = """
        <section id="people" class="hide">
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
