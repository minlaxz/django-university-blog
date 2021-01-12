console.log('home.js is loaded.')

document.getElementById('blog').addEventListener('click', blog )

document.getElementById('about').addEventListener('click', about )

document.getElementById('admin').addEventListener('click', admin )

function blog() {
    window.location.href = 'blog'
}

function about() {
    window.location.href = 'about'
}

function admin() {
    window.location.href = 'admin'
}