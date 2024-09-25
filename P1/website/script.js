document.addEventListener('DOMContentLoaded', function() {
    const tryButton = document.getElementById('tryButton');
    const result = document.getElementById('result');

    tryButton.addEventListener('click', function() {
        const messages = [
            "Hahaha, vraiment ?!",
            "Encore raté, novice !",
            "Il te faut plus qu’un clic pour m’avoir...",
            "Sérieusement, tu crois que c’est aussi facile ?!",
            "Toujours pas, gamin !"
        ];
        const randomMessage = messages[Math.floor(Math.random() * messages.length)];
        result.textContent = randomMessage;
        
        setTimeout(function() {
            result.textContent = '';
        }, 3000);
    });
});
