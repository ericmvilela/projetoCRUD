const toggleDark = document.querySelector('#toggle-theme')
const theme = localStorage.getItem('theme')

if(theme !== null){
    if(theme === 'dark'){
        document.body.classList.add('dark')
        toggleDark.checked = true;
    }
}
else{
    const darkTheme = window.matchMedia("(prefers-color-scheme: dark)")
    if(darkTheme){
        localStorage.setItem('theme', 'dark');
        document.body.classList.add('dark')
        toggleDark.checked = true;
    }
    else {
        localStorage.setItem('theme', 'ligth');
    }

}

toggleDark.addEventListener('change', ()=> {
    document.body.classList.toggle('dark')
    if(document.body.classList.contains('dark')) {
        localStorage.setItem('theme', 'dark');
    }
    else {
        localStorage.setItem('theme', 'ligth');
    }
})

function deletar(url){
    fetch(url, {
        'method': 'DELETE'})
    .then(res => res.json())
    .then(res => location.reload())
    .catch(err => console.log(err))
}