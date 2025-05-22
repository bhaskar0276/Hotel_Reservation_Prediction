## 🚀 Live Demo (Hosted on Google Cloud Run)

You can access the deployed ML prediction application using the link below:

🔗 [Live App URL](https://ml-project-655436918862.us-central1.run.app/)

### 🔐 Access Permissions

✅ This app is **publicly accessible** — no login or API key required.

If you deploy this app yourself to Cloud Run and want others to access it:

- Go to **Cloud Run > your service > Permissions**
- Click **"Add Principal"**
- Add: `allUsers`
- Assign Role: **Cloud Run > Cloud Run Invoker**
- Click **Save**

📢 This makes your endpoint accessible to anyone with the link (like a public website).

---

## 🛠️ How to Run Locally (Optional)

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/Hotel_Reservation_Prediction.git
cd Hotel_Reservation_Prediction

# Install requirements
pip install -r requirements.txt

# Run the Flask app
python application.py
