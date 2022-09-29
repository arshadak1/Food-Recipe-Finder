const fname = document.getElementById('fname')
const lname = document.getElementById('lname')
const email = document.getElementById('email')
const password = document.getElementById('password')
const confirm_password = document.getElementById('confirm-password')



const checkFname = () => {
    if (!isalpha(fname.value)) {
        const input = document.getElementById('fname-div')
        input.classList.add('error')
        input.querySelector('small').style.visibility = 'visible'
    }
    else {
        const input = document.getElementById('fname-div')
        input.classList.remove('error')
        input.querySelector('small').style.visibility = 'hidden'
    }
}

const checkLname = () => {
    if (!isalpha(lname.value)) {
        const input = document.getElementById('lname-div')
        input.classList.add('error')
        input.querySelector('small').style.visibility = 'visible'

    }
    else {
        const input = document.getElementById('fname-div')
        input.classList.remove('error')
        input.querySelector('small').style.visibility = 'hidden'
    }
}

const validateForm = (e) => {
    e.preventDefault()
    if (!isalpha(lname.value) || !isalpha(lname.value)) {
        return false
    }

    if (!emailValidator(email.value)) {
        const input = document.getElementById('email-div')
        input.classList.add('error')
        input.querySelector('small').style.visibility = 'visible'
        input.querySelector('small').innerText = 'from js'

        return false
    }
    else {
        const input = document.getElementById('email-div')
        input.classList.remove('error')
        input.querySelector('small').style.visibility = 'hidden'
    }

    document.getElementById('form').submit()
    return true

}

fname.addEventListener('keypress', checkFname)
lname.addEventListener('keypress', checkLname)


const isalpha = (str) => /^[a-zA-Z ]+$/.test(str)
const emailValidator = (email) => /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)