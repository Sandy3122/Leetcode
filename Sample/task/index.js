const express = require("express");
const admin = require("firebase-admin");
const jwt = require("jsonwebtoken");
const bcrypt = require("bcrypt");
const cookieParser = require("cookie-parser");

const app = express();

// Initialize Firebase Admin SDK
const serviceAccount = require("./serviceAccountKey.json");
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});

const secretKey =
  process.env.JWT_SECRET_KEY || "e1e5bbbc741d0a216656ebeea990fbba";

// Set up middleware to parse JSON requests
// Use built-in body parser
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Use cookie parser middleware
app.use(cookieParser());

// Serve HTML forms
app.get("/register", (req, res) => {
  res.sendFile(__dirname + "/register.html");
});

app.get("/login", (req, res) => {
  res.sendFile(__dirname + "/login.html");
});

// Define route handler for the root URL
app.get("/", (req, res) => {
  res.send("Welcome to Home Page");
});


// Register user
app.post("/register", async (req, res) => {
  try {
    // console.log('Form Data:', req.body);
    const {
      firstName,
      lastName,
      mobileNumber,
      email,
      password,
      profileImageUrl,
    } = req.body;


    if(!(firstName && lastName && mobileNumber && email && password)){
      return res.status(400).send(`
      Please Fill all the fields. 
      Click here to <a href="/register">Sign Up</a>`);
    }
    
    // Hash the password
    const saltRounds = process.env.SALT || 10;
    const hashedPassword = await bcrypt.hash(password, saltRounds);

    // Save user data to Firestore
    const userRef = await admin.firestore().collection("users").add({
      firstName,
      lastName,
      mobileNumber,
      email,
      password: hashedPassword,
      profilePic: profileImageUrl, // Save the profile image URL to Firestore
    });

    // Generate JWT token
    const token = jwt.sign({ uid: userRef._id }, secretKey, {
      expiresIn: "1h",
    });

    const loginUrl = "/login"; // Set the login page URL
    res.send(`
      <html>
        <head>
          <title>Registration Successful</title>
        </head>
        <body>
          <h1>Registration Successful!</h1>
          <p>Your account has been successfully registered.</p>
          <p>You can now <a href="${loginUrl}">login here</a>.</p>
        </body>
      </html>
    `);
  } catch (error) {
    console.error(error);
    res.status(500).send("Internal Server Error");
  }
});

// Log in user and generate JWT token
app.post("/login", async (req, res) => {
  try {
    const { mobileNumber, password } = req.body;

    // Verify user credentials
    const userSnapshot = await admin
      .firestore()
      .collection("users")
      .where("mobileNumber", "==", mobileNumber)
      .get();

    if (userSnapshot.empty) {
      res.status(401).send("Invalid credentials");
      return;
    }

    const user = userSnapshot.docs[0].data();
    const isPasswordValid = await bcrypt.compare(password, user.password);

    if (!isPasswordValid) {
      res.status(401).send("Invalid credentials");
      return;
    }

    // Generate JWT token
    const token = jwt.sign({ uid: userSnapshot.docs[0].id }, secretKey, {
      expiresIn: "1h",
    });

    // Set the token in a cookie
    res.cookie("jwtToken", token, { httpOnly: true });

    res.redirect("/profile");


    console.log("Login successful. Redirecting to /profile");
  } catch (error) {
    console.error(error);
    res.status(500).send("Internal Server Error");
  }
});

const jwtMiddleware = (req, res, next) => {
  const token = req.cookies.jwtToken;

  if (!token) {
    return res.status(401).json({ error: "Unauthorized" });
  }

  jwt.verify(token, secretKey, (err, decoded) => {
    if (err) {
      console.error("Error verifying token:", err);
      return res.status(401).json({ error: "Unauthorized" });
    }

    req.userId = decoded.uid;
    next();
  });
};

// Get logged-in user data
app.get("/profile", jwtMiddleware, async (req, res) => {
  try {
    const userId = req.userId;

    console.log("User ID:", userId); // Log the user ID

    // Fetch user data from the database
    const userSnapshot = await admin
      .firestore()
      .collection("users")
      .doc(userId)
      .get();

    if (!userSnapshot.exists) {
      console.log("User not found");
      return res.status(404).json({ error: "User not found" });
    }

    const userData = userSnapshot.data();

    console.log("User Data:", userData); // Log the user data

    res.send(`
    <html>
      <head>
        <title>Dashboard</title>
      </head>
      <body>
        <h1>Welcome, ${userData.firstName} ${userData.lastName}!</h1>
        <img src="${userData.profilePic}" alt="Profile Picture">
        <center><a href="/logout"><button>Log Out</button></a></center>
      </body>
    </html>
  `);
  } catch (error) {
    console.error("Error in /user route:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});




// Logout route
app.get("/logout", (req, res) => {
    res.clearCookie("jwtToken");  
    // Redirect to the login page
    res.redirect("/login");
  });
  

const PORT = process.env.PORT || 3000;
// Start the server
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
