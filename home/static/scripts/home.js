console.log('home.js is loaded.')

document.getElementById('blog').addEventListener('click', blog )

document.getElementById('about').addEventListener('click', about )

function blog() {
    alert("Blog is under construct.")
}

function about() {
    window.location.href = 'about'
}