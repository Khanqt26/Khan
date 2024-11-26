import streamlit as st
import datetime

st.set_page_config(page_title="Khan's Biography", layout="wide")

# Initialize session state if not already initialized
if 'toggle_state' not in st.session_state:
    st.session_state.toggle_state = False
if 'name' not in st.session_state:
    st.session_state.name = "Khan L. Adjarani"
if 'about_me' not in st.session_state:
    st.session_state.about_me = ("Hi Im Khan and I like playing Online games, specially Mobile Legends and I also love watching movies in Netflix and I also love to travel using a motorcycle and enjoy nature.")
if 'mother_name' not in st.session_state:
    st.session_state.mother_name = "Charmaine Ixara Lopez"
if 'father_name' not in st.session_state:
    st.session_state.father_name = "Reymos Adjarani"
if 'mother_bday' not in st.session_state:
    st.session_state.mother_bday = datetime.date(1970, 1, 7)
if 'father_bday' not in st.session_state:
    st.session_state.father_bday = datetime.date(1969, 6, 30)
if 'high_school' not in st.session_state:
    st.session_state.high_school = "Tubod National Highschool"
if 'senior_high_school' not in st.session_state:
    st.session_state.senior_high_school = "St. Paul University Surigao"
if 'college' not in st.session_state:
    st.session_state.college = "Surigao del Norte State University"
if 'hobbies' not in st.session_state:
    st.session_state.hobbies = "- I Code\n- I Play online games\n- Watch Movies\n- Ride a Motorcycle"
if 'gender' not in st.session_state:
    st.session_state.gender = "Male"
if 'birthplace' not in st.session_state:
    st.session_state.birthplace = "Ipil, Zamboanga Sibugay"
if 'current_address' not in st.session_state:
    st.session_state.current_address = "Tubod, Surigao del Norte"
if 'mybirthday' not in st.session_state:
    st.session_state.mybirthday = datetime.date(2005, 11, 3)  # Default birthdate (can be updated)

def toggle_button():
    st.session_state.toggle_state = not st.session_state.toggle_state

st.markdown(
    """
    <div style="text-align: center; font-size: 40px;">
        <strong> Khan's Biography </strong>  
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown("""<div style="text-align: center; font-size: 25px;"><strong>Get to know me</strong></div>""", unsafe_allow_html=True)
        
        st.session_state.name = st.text_input("My Name", st.session_state.name)

        st.text_area("What I do", st.session_state.hobbies, height=125, key='hobbies')
        
        # Add the new fields for Age, Place of Birth, and Current Address
        st.subheader("Personal Details")
        
        # Make the birthdate editable
        birth_date = st.date_input("Date of Birth", st.session_state.mybirthday)
        st.session_state.mybirthday = birth_date  # Update the session state with the new date

        # Calculate age based on the selected birthdate
        st.session_state.age = (datetime.date.today() - birth_date).days // 365  # Calculate age
        st.write(f"Age: {st.session_state.age} years old")
        
        st.session_state.birthplace = st.text_input("Place of Birth", st.session_state.birthplace)
        st.session_state.current_address = st.text_input("Current Address", st.session_state.current_address)
        
        st.markdown("""<div style="text-align: center; font-size: 25px;"><strong>Click to see hobbies and achievements</strong></div>""", unsafe_allow_html=True)
        if st.button("Click here"):
            toggle_button()
        
        if st.session_state.toggle_state:
            st.markdown("""<div style="text-align: center; font-size: 25px;"><strong>Details about hobbies and achievements</strong></div>""", unsafe_allow_html=True)
            st.text_area("Achievements", "- Won 2nd place in Photojournalism in 2018\n- Learn how to drive a car", height=125)
            st.text_area("Game Achievements", "- Reach Mythical Immortal in Mobile Legends\n- Reach Exalted Collector III\n - Obtain Cosmic Gleam\n - Obtain Devine Goddess\n - Top 80 Philippines using Kadita\n - Top 1 Surigao del Norte Terizla", height=125)
        
        st.write("---")
        st.markdown("""<div style="text-align: center; font-size: 25px;"><strong>Social Media Accounts</strong></div>""", unsafe_allow_html=True)

        social_media_html = """
            <a href="https://www.facebook.com/KhanAqt16/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook" width="40" height="40" />
            </a>
            <a href="https://www.youtube.com/@khanadjarani7954" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" alt="YouTube" width="40" height="40" />
            </a>
            <a href="https://www.instagram.com/khanqt_/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/128/174/174855.png" alt="Instagram" width="40" height="40" />
            </a>
        """
        st.markdown(social_media_html, unsafe_allow_html=True)

    with right_column:
        # Image uploader to allow changing the profile picture
        uploaded_image = st.file_uploader("Upload a new profile picture", type=["png", "jpg", "jpeg"])
        if uploaded_image is not None:
            st.image(uploaded_image, width=250)
        else:
            st.image("https://scontent.fceb1-5.fna.fbcdn.net/v/t39.30808-1/468079930_1723962661722396_6503818840938910621_n.jpg?stp=cp6_dst-jpg_s200x200_tt6&_nc_cat=102&ccb=1-7&_nc_sid=0ecb9b&_nc_eui2=AeH97i42yyM7CILuOB-rP0LE_pylAQbkd4v-nKUBBuR3i1MDDN-X-xynvequiSAUiP6-SUPzD5rPVgKv2K-PO-2-&_nc_ohc=P0M-o1l7uy4Q7kNvgFArB4C&_nc_zt=24&_nc_ht=scontent.fceb1-5.fna&_nc_gid=ANK_Q9DqxCeuE40RFus10c9&oh=00_AYAoMDmGsM8DogwEFhVBOm69G-xI694A6JgJyyMUwdAgMA&oe=6749093B", width=250)
        
        st.markdown("""<div style="text-align: center; font-size: 25px;"><strong>ABOUT ME</strong></div>""", unsafe_allow_html=True)       
        
        st.session_state.about_me = st.text_area("About Me", st.session_state.about_me, height=200)
        st.session_state.gender = st.radio("Gender", ["Male", "Female"], index=0 if st.session_state.gender == "Male" else 1)

        st.subheader("Family Background")
        st.session_state.mother_name = st.text_input("Mother's Name", st.session_state.mother_name)
        st.session_state.mother_bday = st.date_input("Mother's Birthday", st.session_state.mother_bday)
        st.session_state.father_name = st.text_input("Father's Name", st.session_state.father_name)
        st.session_state.father_bday = st.date_input("Father's Birthday", st.session_state.father_bday)
        
        st.subheader("Educational Attainment")
        st.session_state.high_school = st.text_input("High School", st.session_state.high_school)
        st.session_state.senior_high_school = st.text_input("Senior High School", st.session_state.senior_high_school)
        st.session_state.college = st.text_input("College", st.session_state.college)
        
        st.write("---")
