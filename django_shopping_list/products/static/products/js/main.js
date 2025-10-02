// Função para adicionar produto
async function addProduct() {
    const name = document.getElementById('product-name').value.trim();
    const price = document.getElementById('product-price').value;
    const quantity = document.getElementById('product-quantity').value || 1;

    if (!name || !price) {
        showMessage('Por favor, preencha nome e preço do produto', 'error');
        return;
    }

    if (parseFloat(price) <= 0) {
        showMessage('O preço deve ser maior que zero', 'error');
        return;
    }

    showLoading(true);

    try {
        const response = await fetch('/add/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: name,
                price: parseFloat(price),
                quantity: parseInt(quantity)
            })
        });

        const data = await response.json();

        if (data.success) {
            showMessage('Produto adicionado com sucesso!', 'success');
            // Limpar formulário
            clearForm();
            // Recarregar página após pequeno delay
            setTimeout(() => {
                location.reload();
            }, 1000);
        } else {
            showMessage('Erro ao adicionar produto', 'error');
        }
    } catch (error) {
        console.error('Erro:', error);
        showMessage('Erro ao adicionar produto', 'error');
    } finally {
        showLoading(false);
    }
}

// Função para alternar status de comprado
async function togglePurchased(productId) {
    showLoading(true);
    
    try {
        const response = await fetch(`/toggle/${productId}/`, {
            method: 'POST'
        });

        if (response.ok) {
            const data = await response.json();
            showMessage(data.purchased ? 'Produto marcado como comprado' : 'Produto desmarcado', 'success');
            setTimeout(() => {
                location.reload();
            }, 500);
        } else {
            showMessage('Erro ao atualizar produto', 'error');
        }
    } catch (error) {
        console.error('Erro:', error);
        showMessage('Erro ao atualizar produto', 'error');
    } finally {
        showLoading(false);
    }
}

// Função para deletar produto
async function deleteProduct(productId) {
    if (!confirm('Deseja remover este produto da lista?')) {
        return;
    }

    showLoading(true);

    try {
        const response = await fetch(`/delete/${productId}/`, {
            method: 'POST'
        });

        if (response.ok) {
            showMessage('Produto removido com sucesso!', 'success');
            setTimeout(() => {
                location.reload();
            }, 1000);
        } else {
            showMessage('Erro ao deletar produto', 'error');
        }
    } catch (error) {
        console.error('Erro:', error);
        showMessage('Erro ao deletar produto', 'error');
    } finally {
        showLoading(false);
    }
}

// Função para atualizar quantidade
async function updateQuantity(productId, quantity) {
    if (quantity < 1) {
        showMessage('A quantidade deve ser maior que zero', 'error');
        return;
    }

    showLoading(true);

    try {
        const response = await fetch(`/update-quantity/${productId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                quantity: parseInt(quantity)
            })
        });

        if (response.ok) {
            showMessage('Quantidade atualizada!', 'success');
            setTimeout(() => {
                location.reload();
            }, 500);
        } else {
            showMessage('Erro ao atualizar quantidade', 'error');
        }
    } catch (error) {
        console.error('Erro:', error);
        showMessage('Erro ao atualizar quantidade', 'error');
    } finally {
        showLoading(false);
    }
}

// Função para alterar quantidade com botões +/-
function changeQuantity(productId, change) {
    const input = document.querySelector(`[data-id="${productId}"] .quantity-input`);
    const newQuantity = parseInt(input.value) + change;
    
    if (newQuantity >= 1) {
        updateQuantity(productId, newQuantity);
    }
}

// Função para limpar formulário
function clearForm() {
    document.getElementById('product-name').value = '';
    document.getElementById('product-price').value = '';
    document.getElementById('product-quantity').value = '1';
    document.getElementById('product-name').focus();
}

// Função para mostrar mensagens
function showMessage(message, type = 'info') {
    // Remove mensagem anterior se existir
    const existingMessage = document.querySelector('.message');
    if (existingMessage) {
        existingMessage.remove();
    }

    const messageDiv = document.createElement('div');
    messageDiv.className = `message message-${type}`;
    messageDiv.textContent = message;
    
    // Estilos para a mensagem
    messageDiv.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 20px;
        border-radius: 10px;
        color: white;
        font-weight: bold;
        z-index: 1000;
        transition: all 0.3s ease;
        max-width: 300px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    `;
    
    // Cores baseadas no tipo
    switch (type) {
        case 'success':
            messageDiv.style.background = 'linear-gradient(135deg, #28a745, #20c997)';
            break;
        case 'error':
            messageDiv.style.background = 'linear-gradient(135deg, #dc3545, #fd7e14)';
            break;
        default:
            messageDiv.style.background = 'linear-gradient(135deg, #007bff, #6f42c1)';
    }
    
    document.body.appendChild(messageDiv);
    
    // Remover após 3 segundos
    setTimeout(() => {
        messageDiv.style.opacity = '0';
        messageDiv.style.transform = 'translateX(100%)';
        setTimeout(() => {
            if (messageDiv.parentNode) {
                messageDiv.remove();
            }
        }, 300);
    }, 3000);
}

// Função para mostrar/esconder loading
function showLoading(show) {
    const container = document.querySelector('.container');
    if (show) {
        container.classList.add('loading');
    } else {
        container.classList.remove('loading');
    }
}

// Configurações quando a página carrega
document.addEventListener('DOMContentLoaded', function() {
    // Permitir adicionar produto com Enter em qualquer campo do formulário
    const inputs = document.querySelectorAll('#product-name, #product-price, #product-quantity');
    inputs.forEach(input => {
        input.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                addProduct();
            }
        });
    });

    // Focar no primeiro campo ao carregar
    const firstInput = document.getElementById('product-name');
    if (firstInput) {
        firstInput.focus();
    }

    // Validação em tempo real para preço
    const priceInput = document.getElementById('product-price');
    if (priceInput) {
        priceInput.addEventListener('input', function() {
            if (this.value < 0) {
                this.value = 0;
            }
        });
    }

    // Validação em tempo real para quantidade
    const quantityInput = document.getElementById('product-quantity');
    if (quantityInput) {
        quantityInput.addEventListener('input', function() {
            if (this.value < 1) {
                this.value = 1;
            }
        });
    }

    // Adicionar animação de entrada para os itens da lista
    const productItems = document.querySelectorAll('.product-item');
    productItems.forEach((item, index) => {
        item.style.opacity = '0';
        item.style.transform = 'translateY(20px)';
        setTimeout(() => {
            item.style.transition = 'all 0.3s ease';
            item.style.opacity = '1';
            item.style.transform = 'translateY(0)';
        }, index * 100);
    });

    console.log('Lista de Compras carregada com sucesso!');
});