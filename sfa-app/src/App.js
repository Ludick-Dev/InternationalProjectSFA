import "./App.css";
import "./Script.js";
import Other7 from "./Images/Other 07.png";
import ASLImg1 from "./Images/ASL Image.jpg";
import ASLImg2 from "./Images/ASL_Image.jpg";
import Other17 from "./Images/Other 17.png";

function App() {
  return (
    <div>
      
      <div>
      <header>
      <a href="#" class="logo">Translate Sign!</a>
      <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#Translate_Section">Translate</a></li>
        <li><a href="#More_Info">More Info</a></li>
        <li><a href="#About_Us">About Us</a></li>
      </ul>
    </header>
    
    
      </div>

      <section class="Home" id="home">
        <br />
        <br />
        <div id="homeText">
          <h1 class="Heading1">Sign To Text Translation</h1>
          <p class="subheading">
            The future of breaking the barrier between sign language
            communication.
          </p>
          <section class="container2">
            <section class="box1">
              <p>
                Welcome to Sign For All, the cutting-edge sign language to text
                conversion tool developed in collaboration with Fontys and PXL.
                Our goal is to make communication more accessible and inclusive
                for people who use sign language as their primary means of
                communication.
              </p>
            </section>
            <aside class="box 2">
              <img src={Other7} alt="Image 1" />
            </aside>
          </section>
          <br />
          <p>
            Our program uses advanced artificial intelligence and computer
            vision techniques to interpret and translate sign language gestures
            into written text in real-time. This means that our tool can help
            bridge the communication gap between sign language users and
            non-sign language users, enabling them to communicate more easily
            and effectively. Sign For All is easy to use and can be accessed
            through a variety of devices, including smartphones, tablets, and
            computers.
          </p>
          <section class="container2">
            <aside>
              <img src={Other17} alt="Image 2" />
            </aside>
            <section class="box1">
              <p>
                MediaPipe is an open-source cross-platform framework for
                building multimodal machine learning applications, designed to
                process and analyze perceptual data such as video and audio
                streams.
              </p>
            </section>
          </section>
        </div>
      </section>

      <section class="Translation-Section" id="Translate_Section">
        <h1 class="Heading1">Translate Here!</h1>
        <div class="container5">
          <div class="video-container5">
            <div id="container1">
              <video autoplay="true" id="videoElement"></video>
            </div>
          </div>
          <div class="text-box5">
            <p>Translation Text Here (Example of where the text must be)</p>
          </div>
        </div>
      </section>

      <br />
      <br />
      <section class="More_Info" id="More_Info">
        <h1 class="Heading1">Learning Sign Language</h1>
        <div class="container2">
          <section class="box1">
            <p class="par">
              The future of the breaking the barrier between sign language
              communication. The goal of creating this application is to help
              deaf people speak with normal people with ease, and vice versa.
            </p>
          </section>
          <aside class="box2">
            <img src={ASLImg2} alt="" srcset="ASL Picture" />
          </aside>
        </div>

        <br />
        <h1 class="Heading1">Don't know where to start?</h1>
        <div class="container3">
          <section class="box3">
            <img src={ASLImg1} alt="Image 3" srcset="" />
          </section>
          <aside class="box4">
            <p class="par">
              If you didn't know where to start, let's make it simple. Learn the
              alphabet. Although it might seem daunting and tedious in the
              beginning, learning the alphabet is the most crucial part.
            </p>
            <br />
            <p class="par">
              Below are some links that can be used as resources to learn sign
              language:
            </p>
            <ul>
              <li>
                <a
                  href="https://www.startasl.com/"
                  class="links"
                  target="_blank"
                >
                  Start ASL
                </a>
                - This website offers a variety of resources for learning ASL,
                including online courses, a dictionary, and articles on deaf
                culture. They also have a YouTube channel with video lessons
              </li>
              <li>
                <a
                  href="http://lifeprint.com/asl101/"
                  class="links"
                  target="_blank"
                >
                  ASL University
                </a>
                - This website offers free online ASL lessons, including video
                tutorials and printable resources. The lessons cover vocabulary,
                grammar, and syntax, as well as deaf culture.
              </li>
              <li>
                <a
                  href="https://www.youtube.com/c/ASLMeredith"
                  class="links"
                  target="_blank"
                >
                  ASL Meredith
                </a>
                - This YouTube channel offers video lessons on ASL, ranging from
                beginner to advanced levels. The lessons cover vocabulary,
                grammar, and syntax, as well as tips for practicing and using
                ASL in real-world situations.
              </li>
              <li>
                <a
                  href="https://www.signingsavvy.com/"
                  class="links"
                  target="_blank"
                >
                  Signing Savvy
                </a>
                - This website offers a dictionary of ASL signs, as well as
                video lessons and quizzes to help you practice your skills. They
                also have a blog with tips and resources for learning and using
                ASL.
              </li>
            </ul>
          </aside>
        </div>
      </section>

      <br />
      <br />
      <br />
      <section class="About-Us" id="About_Us">
        <h1 class="Heading1">About Us</h1>
        <div id="aboutText">
          <h2>Belgium Campus</h2>
          <p class="aText">
            <b>Mission:</b> To supply the industry with highly qualified and
            experienced Information Technology personnel by providing
            high-quality, practice-orientated education and training of an
            International standard. We know this will contribute to economic
            growth and wealth creation. <br />
            <br />
            Belgium Campus iTversity is at the forefront of what a modern
            university should be. By investing in people, attracting investors,
            running community programmes and engaging with local communities and
            authorities, we ensure that this sentiment is adhered to. We conduct
            our operations in the spirit of ubuntu – for the benefit of all.
            <br />
            <br />
            <b>Vision:</b> To transform South Africa into a prosperous nation.
            There is a great demand for highly skilled graduates with the right
            competencies, and higher education has a big role to play in this
            development process. We realise we have to do things differently
            from other universities. The strategy of a university should and
            must make a significant impact on regional development by
            cooperating with industry and business and by educating and
            delivering the required workforce on all levels.
            <br />
          </p>
          <h2>Fontys University of Applied Sciences</h2>
          <p class="aText">
            Development is a key concept at Fontys. Young people develop their
            talents as students with us, we develop relevant practical
            knowledge, working professionals can also develop further at Fontys,
            we respond flexibly to far-reaching social developments and – last
            but not least – within our community we develop ourselves by sharing
            knowledge and skills. <br />
            <br />
            We operate in the heart of society. In our hybrid learning and
            research environments, students, lecturers, researchers, and
            professionals work together. In that way, education and research, as
            well as learning and working, become increasingly intertwined. Our
            main social value is therefore the development of talent and
            knowledge. <br />
            <br />
            Fontys is a multidisciplinary university of applied sciences in the
            south of the Netherlands. Together with and for the (regional)
            professional environments, we provide high-quality, higher
            vocational education and conduct innovative, practice-oriented
            research. In this way, we contribute to the development of a
            dynamic, inclusive, and sustainable society. <br />
            <br />
          </p>
          <h2>PXL University of Applied Sciences and Arts</h2>
          <p class="aText">
            <b>Mission:</b> PXL University of Applied Sciences professionalizes
            people and organizations and thus contributes to prosperity and
            well-being. <br />
            <br />
            <b>Vision:</b>Through a strong intertwining of education, research,
            services and the practice of the arts, PXL University of Applied
            Sciences wants its students (junior colleagues) and employees to
            grow further as excellent professionals (= X-factor) and, together
            with its partners, to grow as an excellent professional organization
            (= X-factor). We translate the PXL vision into the X-factor that is
            a model for the 'excellent professional' and for the 'excellent
            professional organization'. We always use 'excellent' in combination
            (-) with 'professional' because we do not strive for excellence per
            se, but for 'excellent professional'. The X-factor is a combination
            of (em)passion, of being enterprising and innovative, of
            (multi)disciplinarity and of (international) collaboration (network)
            working. The X-factor with its 4 overlapping axes, forms a single
            and indivisible whole of hard and soft skills and is more than the
            sum of its parts. The X-factor has a double effect. It is both our
            'look-pointer' and our 'compass'. The look-pointer for
            (self)reflection indicates where we stand at the start, the compass
            shows us the way to the ultimate goal, the excellent professional /
            professional organization. The X-factor is not only a look-pointer
            and a compass for our junior colleagues, our staff and network, but
            also for PXL University of Applied Sciences, as a beacon in its
            pursuit of an excellent professional organization (= X-factor)
            <br />
          </p>
        </div>
      </section>
    </div>
  );
}

export default App;
