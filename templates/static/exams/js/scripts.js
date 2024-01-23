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
    // const checkbox_value = document.getElementById('checkbox_checked')

    const selectedOptions = document.querySelectorAll('.option input:checked');

    console.log('OPTION' + selectedOptions)

    const textarea = document.getElementById('output');

    textarea.value = Array.from(selectedOptions).map(option => option.value).join('\n');

    // if (checkbox_value.checked){
    //     var checkboxValue = checkbox.value;

    //     var checkboxes = document.querySelectorAll('input[type="checkbox"][name="yourCheckboxName"]');
            
    //     // Filter checked checkboxes
    //     var checkedCheckboxes = Array.from(checkboxes).filter(checkbox => checkbox.checked);
        
    //     // Get the names of checked checkboxes
    //     var checkedNames = checkedCheckboxes.map(checkbox => checkbox.getAttribute('name'));

        

    // } else {
    //     console.log("Checkbox is not checked.");
    // }
}
