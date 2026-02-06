document.addEventListener('DOMContentLoaded', function() {
    console.log('force download is enabled!');
    const dropdown = document.querySelector('.dropdown-download-buttons');
    if (dropdown) {
        dropdown.querySelectorAll('a').forEach(a => {
        const href = a.getAttribute('href');
        if (href && (href.endsWith('.md') || href.endsWith('.ipynb'))) {
            console.log(`Adding download attribute to ${href}`);
            if (!a.hasAttribute('download')) {
                a.setAttribute('download', '');
            }
        }
        });
    }
});
