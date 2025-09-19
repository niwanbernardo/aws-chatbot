document.addEventListener('DOMContentLoaded', function() {
    const messageInput = document.getElementById('messageInput');
    const sendButton = document.getElementById('sendButton');
    const chatMessages = document.getElementById('chatMessages');

    // Enviar mensagem ao pressionar Enter
    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    // Enviar mensagem ao clicar no botão
    sendButton.addEventListener('click', sendMessage);

    function sendMessage() {
        const message = messageInput.value.trim();
        
        if (!message) return;

        // Adicionar mensagem do usuário
        addMessage(message, 'user');
        
        // Limpar input e desabilitar botão
        messageInput.value = '';
        sendButton.disabled = true;
        sendButton.innerHTML = '<div class="loading"></div>';

        // Enviar para o servidor
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            // Adicionar resposta do bot
            addMessage(data.response, 'bot');
        })
        .catch(error => {
            console.error('Erro:', error);
            addMessage('❌ Erro de conexão. Tente novamente.', 'bot');
        })
        .finally(() => {
            // Reabilitar botão
            sendButton.disabled = false;
            sendButton.innerHTML = 'Enviar';
            messageInput.focus();
        });
    }

    function addMessage(content, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        
        if (sender === 'bot') {
            // Processar markdown básico para mensagens do bot
            content = content
                .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                .replace(/\*(.*?)\*/g, '<em>$1</em>');
            messageContent.innerHTML = content;
        } else {
            messageContent.textContent = content;
        }
        
        messageDiv.appendChild(messageContent);
        chatMessages.appendChild(messageDiv);
        
        // Scroll para a última mensagem
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Focar no input ao carregar a página
    messageInput.focus();
});