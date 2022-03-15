       const addRef = document.querySelector('#addForm');
        const formRef = document.querySelector('#emptyForm > div')
        const additionalFormsRef = document.querySelector('#additionalForms')

        addRef.addEventListener('click', (event) => {
            event.preventDefault();

            const formIdxRef = document.querySelector('#id_form-TOTAL_FORMS')
            const idx = parseInt(formIdxRef.value)
            const newForm = formRef.cloneNode(true);

            const elements = newForm.querySelectorAll('[id*="__prefix__"], [name*="__prefix__"], [for*="__prefix__"]')
            elements.forEach((e) => {
                if (e.hasAttribute('id')) {
                    e.id = e.id.replace('__prefix__', idx);
                }
                if (e.hasAttribute('name')) {
                    e.setAttribute('name', e.getAttribute('name').replace('__prefix__', idx))
                }
                if (e.hasAttribute('for')) {
                    e.setAttribute('for', e.getAttribute('for').replace('__prefix__', idx))
                }
            })

            additionalFormsRef.appendChild(newForm);
            formIdxRef.value = idx + 1;
        })


        const deletesRef = document.querySelectorAll('[name$="DELETE"]')

        deletesRef.forEach(element => {
            element.addEventListener('change', (event) => {
                console.log('test')
                event.target.closest('.form').remove();
            })
        })