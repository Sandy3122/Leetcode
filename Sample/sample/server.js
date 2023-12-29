// const crypto = require("crypto");
// randomKey = crypto.randomBytes(16).toString('hex');
// console.log(randomKey)
// // node -e "console.log(require('crypto').randomBytes(16).toString('hex'))"



const express = require("express");
const app = express();
const dotenv = require("dotenv");


app.use(express.json());
app.use(express.urlencoded({extended: true}));

const admin = require("firebase-admin");

const credentials = require("../firebase-auth/serviceAccountKey.json");

admin.initializeApp({
    credential: admin.credential.cert(credentials),
});

app.post("/signup", async(req, res) => {
    console.log(req)
    try{
        const user = {
            email:req.body.email,
            password: req.body.password
        }
        const userResponse = await admin.auth().createUser({
            email: user.email,
            password: user.password,
            emailVerified: false,
            disabled: false
        });
        res.json(userResponse);
    }
    catch(err){
        console.log(err)
    }
})


const PORT = process.env.PORT || "8080";
app.listen(PORT, () => {
    console.log(`Server Started: http://localhost:${PORT}`);
})