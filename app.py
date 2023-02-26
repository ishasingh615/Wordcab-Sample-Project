import streamlit as st
import io
import streamlit.components.v1 as components
import requests
import time 
import pymongo
from dotenv import load_dotenv
load_dotenv()
import os 



client = pymongo.MongoClient(f"mongodb+srv://WordcabSample:{os.getenv('PASSWORD')}@cluster0.tosswts.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

# My attempt to connect the Wordcab's UI components to the application: 
# components.html(
#     """
#    --active-highlight:#eeefff;--player-btn-bg-color:#fff;--player-btn-border-color:#e9ecef;--player-btn-fg-color:#333333;--player-btn-height:36px;--player-btn-hover-bg-color:#fff;--player-btn-hover-fg-color:#353ce7;--player-btn-radius:36px;--player-btn-width:36px;--player-progress-color:#353ce7;--player-timeline-color:#c4c4c4;--primary-color:#353ec7;--range-focus-shadow:0 0 0 0.25rem rgba(83, 89, 235, 0.5);--range-height:32px;--range-thumb-border-radius:24px;--range-thumb-height:24px;--range-thumb-offset:-8px;--range-thumb-width:24px;--range-track-bg:#e9ecef;--range-track-border-radius:8px;--range-track-height:8px;--range-track-width:100%;font-family:Inter,Helvetica,Arial,sans-serif;position:relative}[wordcab-theme] *,[wordcab-theme] ::after,[wordcab-theme] ::before{box-sizing:border-box}[wordcab-player]{align-items:center;display:flex;justify-content:center}[wordcab-player-btn]{-webkit-appearance:none;appearance:none;background-color:var(--player-btn-bg-color);border-radius:var(--player-btn-radius);border:1.5px solid var(--player-btn-border-color);color:var(--player-btn-fg-color);cursor:pointer;display:inline-block;font-size:.875rem;height:var(--player-btn-height);padding:0;transition:all .125s ease-out;vertical-align:middle;width:var(--player-btn-width)}[wordcab-player-btn]:hover{background-color:var(--player-btn-hover-bg-color);border-color:var(--player-btn-hover-fg-color);color:var(--player-btn-hover-fg-color)}[wordcab-player-btn] svg{vertical-align:middle}[wordcab-player-timeline]{background:var(--player-timeline-color);height:41px;position:relative;width:100%;width:212px}[wordcab-player-timeline]>svg{left:0;position:absolute;top:0}[wordcab-player-progress]{background:var(--player-progress-color);height:41px;position:relative;transition:width .25s cubic-bezier(.31, .1, .16, .96);width:4%}[wordcab-player-duration],[wordcab-player-time]{font-size:14px;text-align:center;width:50px}[wordcab-player-scrubber]{appearance:none;cursor:pointer;height:100%;left:0;opacity:0;position:absolute;top:0;width:100%}[wordcab-summary-block]{overflow-x:hidden;overflow-y:auto;position:relative}[wordcab-summary-block] .summary-bullet{border-radius:3px;font-size:1.125em;line-height:2.25em;list-style:none;margin-bottom:1.5em;padding:0 1.5em;position:relative}[wordcab-summary-block] .summary-bullet::before{content:'•';left:.5em;position:absolute;top:0}[wordcab-summary-block] .summary-bullet.active,[wordcab-summary-block] .summary-bullet:hover{background-color:var(--active-highlight)}[wordcab-summary-slider]{align-items:center;display:flex}[wordcab-summary-slider]>div:first-child{padding-right:8px}[wordcab-summary-slider]>div:last-child{padding-left:8px}[wordcab-summary-slider]>div:nth-child(2){flex:1 0 0%}[wordcab-range-progress]{position:relative}[wordcab-summary-length]{appearance:none;background-color:transparent;height:var(--range-height);margin:0;padding:0;width:100%}[wordcab-summary-length]:focus{outline:0}[wordcab-summary-length]::-webkit-slider-thumb{box-shadow:var(--range-focus-shadow)}[wordcab-summary-length]::-moz-range-thumb{box-shadow:var(--range-focus-shadow)}[wordcab-summary-length]::-moz-focus-outer{border:0}[wordcab-summary-length]::-webkit-slider-thumb{appearance:none;background-color:var(--primary-color);border-radius:var(--range-thumb-border-radius);border:var(--range-thumb-border);box-shadow:var(--range-thumb-box-shadow);height:var(--range-thumb-height);margin-top:var(--range-thumb-offset);transition:all .125s ease;width:var(--range-thumb-width)}[wordcab-summary-length]::-webkit-slider-runnable-track{background-color:var(--range-track-bg);border-color:transparent;border-radius:var(--range-track-border-radius);box-shadow:var(--range-track-box-shadow);color:transparent;cursor:pointer;height:var(--range-track-height);width:var(--range-track-width)}[wordcab-summary-length]::-moz-range-thumb{appearance:none;background-color:var(--primary-color);border-radius:var(--range-thumb-border-radius);border:var(--range-thumb-border);box-shadow:var(--range-thumb-box-shadow);height:var(--range-thumb-height);transition:all .125s ease;width:var(--range-thumb-width)}[wordcab-summary-length]::-moz-range-track{background-color:var(--range-track-bg);border-color:transparent;border-radius:var(--range-track-border-radius);box-shadow:var(--range-track-box-shadow);color:transparent;cursor:pointer;height:var(--range-track-height);width:var(--range-track-width)}[wordcab-summary-length]:disabled{opacity:.5;pointer-events:none}[wordcab-range-progress]::before{background-color:var(--primary-color);border-bottom-left-radius:1em;border-top-left-radius:1em;content:"";height:8px;left:0;pointer-events:none;position:absolute;top:.75rem;width:var(--range-width);z-index:1}[wordcab-range-progress] .range-ticks{left:0;position:absolute;right:0;top:0;z-index:-1}[wordcab-range-progress] .range-tick{background-color:#dee2e6;display:block;height:19px;position:absolute;top:7px;width:2px}[wordcab-range-progress][data-range="3"] .range-tick:nth-child(1){left:50%;transform:translateX(-1px)}[wordcab-range-progress][data-range="4"] .range-tick:nth-child(1){left:33.3333%;transform:translateX(3px)}[wordcab-range-progress][data-range="5"] .range-tick:nth-child(1){left:25%;transform:translateX(5px)}[wordcab-range-progress][data-range="4"] .range-tick:nth-child(2){left:66.6666%;transform:translateX(-5px)}[wordcab-range-progress][data-range="5"] .range-tick:nth-child(2){left:50%;transform:translateX(-1px)}[wordcab-range-progress][data-range="5"] .range-tick:nth-child(3){left:75%;transform:translateX(-7px)}[wordcab-transcript-block]{overflow-x:hidden;overflow-y:auto}[wordcab-transcript-block] .transcript-utterance{font-size:1rem;line-height:1.75em;margin-bottom:1.25em}[wordcab-transcript-block] .transcript-utterance__ts{border-radius:3px;display:inline-block}[wordcab-transcript-block] .transcript-utterance.active .transcript-utterance__ts{background-color:var(--active-highlight)
#     """
# )


st.title('Wordcab Customer Service Summaries')
st.write("Our service will provide you with a comprehensive and accurate summary of your customer service calls.")

# User input
summary_length = st.number_input('Select your Summary Length: ', min_value=1, max_value=5)

option = st.selectbox(
    'Select your Source Type: ',
    ('Audio File', 'Generic', 'Transcript'))

# Show sample .txt file format 
if (option == "Transcript"):
    st.write("Sample .txt File: ")
    sample_txt = """[00:00:08 --> 00:00:11] Lauren: Thank you for calling Nissan. My name is Lauren. Can I have your name?\n 
[00:00:11 --> 00:00:13] Sam: Yeah, my name is John Smith.\n 
[00:00:13 --> 00:00:15] Lauren: Thank you, John. How can I help you?\n
[00:00:16 --> 00:00:20] Sam: I was just calling about to see how much it would cost to update the map in my car."""
    st.code(sample_txt, language="python")

upload_file = st.file_uploader('Upload File: ')

api_key = st.text_input('Enter your API Key: ')

press = st.button('Submit') 

# Example Summary expandable 
if (not press):
    with st.expander("Sample summary: "): 
        st.write("""SPEAKER A talks about how holderman's notes are the only recollection of what he told them. SPEAKER A notes that they were concerned about a public relations offensive. 
        SPEAKER A says there was no cover up of criminal activities.""")


# After the user submits all their info, run Wordcab's API 
if (press):
    container = st.empty()
    if not upload_file:
        upload_file = open("/Users/ishasingh/Wordcab3/WordcabTest.m4a", "rb")
    #file_path = upload_file.name
    st.write("Preparing your summary. This may take a few minutes.")

    base_url = "https://wordcab.com/api/v1/"

    initiation_url = base_url + "summarize"

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + api_key
    }

    params = {
        "display_name": "Audio File Summary",
        "source": "audio",         
        "summary_type": "narrative",
        "summary_lens": summary_length
    }

    files = {
        #"transcript": open(file_path, "rb")
        # "transcript": open(upload_file.getvalue, "rb")
        "transcript": upload_file
    }

    # Initiating the summary
    initiation_response = requests.post(initiation_url, headers=headers, params=params, files=files)
    job_name = initiation_response.json().get("job_name")

    # Polling the API 
    poll_url = base_url + "jobs?job_name=" + job_name
    poll_response = requests.get(poll_url, headers=headers)

    # Provide the user with a status update every second
    p = st.empty()
    while poll_response.json().get("results")[0].get("job_status") != "SummaryComplete":
        poll_response = requests.get(poll_url, headers=headers)
        p.subheader("Status: " + poll_response.json().get("results")[0].get("job_status"))
        time.sleep(1)

    summary_id = poll_response.json().get("results")[0].get("summary_details").get("summary_id")

    # Retrieving the summary
    retrieve_url = base_url + "summaries/" + summary_id
    retrieve_response = requests.get(retrieve_url, headers=headers)

    # Print the summary on the page
    st.subheader("Your summary: ")
    container = st.empty()
    container.write(retrieve_response.json().get("summary").get(str(summary_length)).get("structured_summary")[0].get("summary"))