const express = require('express');
const multer = require('multer');
const ffmpegPath = require('@ffmpeg-installer/ffmpeg').path;
const ffmpeg = require('fluent-ffmpeg');
ffmpeg.setFfmpegPath(ffmpegPath);
const fs = require('fs');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');


const { exec } = require('child_process');

const app = express();

app.use("/", express.static(__dirname + "/"));

app.use(express.json());

app.get("/", function (req, res) {
  res.sendFile(__dirname + "/index.html");
});

// Add this middleware to enable CORS
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', 'http://localhost:9000'); // Update with your frontend URL
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.header('Access-Control-Allow-Headers', 'Content-Type');
  next();
});

const port = process.env.PORT || 9000;

const server = app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

mongoose.connect(`mongodb+srv://shivakerur99:shivanand99805257@cluster0.usva3cf.mongodb.net/`)
.then(() => {
  console.log('Connected to MongoDB');
})
.catch((err) => {
  console.error('MongoDB connection error:', err);
});

const conversionSchema = new mongoose.Schema({
  filename: String,
  text: String,
  timestamp: Date,
});

const Conversion = mongoose.model('Conversion', conversionSchema);

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  },
});
const upload = multer({ storage });

app.use(bodyParser.json());

app.post('/upload', upload.single('media'), async (req, res) => {
  try {
    const filePath = `uploads/${req.file.originalname}`;
    const text = await convertMediaToText(filePath);

    const conversion = new Conversion({
      filename: req.file.originalname,
      text,
      timestamp: new Date(),
    });

    await conversion.save();
    console.log(conversion);

    res.json({ text });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'An error occurred' });
  }
});
  

app.get('/conversions/:id', async (req, res) => {
  try {
    const conversions = await Conversion.findById(req.params.id);
    // const conversions = await Conversion.find({}, '-_id -__v');
    res.json(conversions);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'An error occurred' });
  }
});

exec('python -m pip install --upgrade pip', (err, stdout, stderr) => {
  if (err) {
    console.error(`Error: ${err}`);
    return;
  }
  console.log(`stdout: ${stdout}`);
  console.error(`stderr: ${stderr}`);

  // Now, you can proceed with other commands or tasks
});
// Run pip install for Python dependencies
exec('python3 pip install -r requirements.txt', (err, stdout, stderr) => {
  if (err) {
    console.error(`Error: ${err}`);
    return;
  }
  console.log(`stdout: ${stdout}`);
  console.error(`stderr: ${stderr}`);
});


async function convertMediaToText(filePath) {
  // Check if the file is a video and extract audio
  if (filePath.endsWith('.mp4')) {
      await new Promise((resolve, reject) => {
          ffmpeg(filePath)
              .toFormat('wav')
              .on('end', resolve)
              .on('error', reject)
              .save('audio.wav');
      });
      filePath = 'audio.wav';
  }
  else if (filePath.endsWith('.mp3')) {
      await new Promise((resolve, reject) => {
          ffmpeg(filePath)
              .toFormat('wav')
              .on('end', resolve)
              .on('error', reject)
              .save('audio2.wav');
      });
      filePath = 'audio2.wav';
  }

  try {
      const text = await convertToText(filePath);
      return text;  // Return the result from convertToText
  } catch (error) {
      console.error(error);
  }

  async function convertToText(filePath) {
      // Construct the Python command with the filePath variable
      const command = `python main.py ${filePath}`; // Replace 'main.py' with your Python script's file name

      return new Promise((resolve, reject) => {
          exec(command, (error, stdout, stderr) => {
              if (error) {
                  console.error(`Error executing Python script: ${error}`);
                  reject(error);
                  return;
              }

              if (stderr) {
                  console.error(`Python script encountered an error: ${stderr}`);
                  reject(stderr);
                  return;
              }  
              resolve(stdout); 
          });
      })
  }
}
