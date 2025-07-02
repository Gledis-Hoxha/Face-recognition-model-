from flask import Flask, render_template
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

# Set up Google Sheets credentials
scope = ['https://www.googleapis.com/auth/drive']
json_keyfile_path = r'face-recognition-credentials.json'  # Update this with the path to your JSON keyfile
creds = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile_path, scope)
client = gspread.authorize(creds)

# Specify the Google Sheets document by its URL
sheet_url = "https://docs.google.com/spreadsheets/d/1FvV0U8OOtMRFItP2XbrlHPiFaPoa-xwDTRF4AMVbVGI/edit?gid=0#gid=0"

# Open the Google Sheets document
doc = client.open_by_url(sheet_url)
sheet = doc.worksheet("Face")

def fetch_data():
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    # Rename columns if necessary
    df = df.rename(columns={
        'YourNewIdentityColumn': 'Identity',
        'YourNewEmotionColumn': 'Emotion'
    })
    return df

@app.route('/')
def index():
    df = fetch_data()

    # Update column names if they're different in your new sheet
    face_counts = df['Identity'].value_counts().reset_index()
    face_counts.columns = ['Identity', 'Count']
    face_fig = px.bar(face_counts, x='Identity', y='Count', title='Your New Face Detection Title', color='Identity',
                      color_discrete_sequence=px.colors.qualitative.Bold)

    mood_counts = df['Emotion'].value_counts().reset_index()
    mood_counts.columns = ['Emotion', 'Count']
    mood_fig = px.bar(mood_counts, x='Emotion', y='Count', title='Your New Mood Detection Title', color='Emotion',
                      color_discrete_sequence=px.colors.qualitative.Pastel)

    # Convert plots to HTML
    face_plot = pio.to_html(face_fig, full_html=False)
    mood_plot = pio.to_html(mood_fig, full_html=False)

    return render_template('index.html', face_plot=face_plot, mood_plot=mood_plot)

if __name__ == '__main__':
    app.run(debug=True)

#%%
