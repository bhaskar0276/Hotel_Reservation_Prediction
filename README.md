## 🚀 Live Demo (Hosted on Google Cloud Run)

You can access the deployed ML prediction application using the link below:

🔗 [Live App URL](https://ml-project-655436918862.us-central1.run.app/)


## 🛠️ How to Run Locally (Optional)

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/Hotel_Reservation_Prediction.git
cd Hotel_Reservation_Prediction

# Install requirements
pip install -r requirements.txt

# Run the Flask app
python application.py



1. **Run Jenkins with the Docker socket mounted**:

```bash
docker run -d \
  --name jenkins-dind \
  -p 8080:8080 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins-custom-image

2. **Manually grant Docker access inside the container:

docker exec -u root -it jenkins-dind bash

# Inside container as root:
usermod -aG docker jenkins
chown root:docker /var/run/docker.sock
chmod 660 /var/run/docker.sock

2. **Restart the container:
docker restart jenkins-dind


