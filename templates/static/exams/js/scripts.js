document.addEventListener('click', function (event) {
    const isClickInside = document.getElementById('custom-select-container').contains(event.target);
    const optionsContainer = document.getElementById('options-container');
    if (!isClickInside && optionsContainer.style.display === 'block') {
        optionsContainer.style.display = 'none';
    }
});

function toggleOptions() {
    const optionsContainer = document.getElementById('options-container');
    optionsContainer.style.display = optionsContainer.style.display === 'none' ? 'block' : 'none';
}

function getAllSelectedValues() {
    const selectedOptions = document.querySelectorAll('.option input:checked');
    const textarea = document.getElementById('output');
    textarea.value = Array.from(selectedOptions).map(option => option.value).join('\n');
}
