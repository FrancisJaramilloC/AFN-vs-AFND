// Control de Secciones (SPA)
function mostrarSeccion(idSeccion) {
    document.querySelectorAll('.seccion-vista').forEach(sec => {
        sec.classList.add('hidden');
    });
    const seccion = document.getElementById(idSeccion);
    if (seccion) {
        seccion.classList.remove('hidden');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    console.log("Aplicación iniciada.");
    
    // Mostrar solo inicio por defecto
    mostrarSeccion('inicio');
    
    const formEj1 = document.getElementById('form-ej1');
    if (formEj1) {
        formEj1.addEventListener('submit', async (e) => {
            e.preventDefault();
            const cadena = document.getElementById('cadena-ej1').value.trim();
            const btn = formEj1.querySelector('button');
            btn.disabled = true;
            btn.textContent = 'Evaluando...';
            
            const resultado = await evaluarCadena(1, cadena);
            
            btn.disabled = false;
            btn.textContent = 'Evaluar Cadena';
            
            mostrarResultadoEj1(resultado);
        });
    }
    const formEj2 = document.getElementById('form-ej2');
    if (formEj2) {
        formEj2.addEventListener('submit', async (e) => {
            e.preventDefault();
            const cadena = document.getElementById('cadena-ej2').value.trim();
            const btn = formEj2.querySelector('button');
            btn.disabled = true;
            btn.textContent = 'Evaluando...';
            
            const resultado = await evaluarCadena(2, cadena);
            
            btn.disabled = false;
            btn.textContent = 'Evaluar Cadena';
            
            mostrarResultadoEj2(resultado);
        });
    }
    const formEj3 = document.getElementById('form-ej3');
    if (formEj3) {
        formEj3.addEventListener('submit', async (e) => {
            e.preventDefault();
            const cadena = document.getElementById('cadena-ej3').value.trim();
            const btn = formEj3.querySelector('button');
            btn.disabled = true;
            btn.textContent = 'Evaluando...';
            
            const resultado = await evaluarCadena(3, cadena);
            
            btn.disabled = false;
            btn.textContent = 'Evaluar Cadena';
            
            mostrarResultadoEj3(resultado);
        });
    }
});

function renderizarRecorrido(datos) {
    if (!datos) return '<p class="text-red-500">Error al evaluar</p>';
    
    let html = `<div class="mb-2">
        <span class="font-bold ${datos.aceptada ? 'text-green-600' : 'text-red-600'}">
            ${datos.mensaje}
        </span>
    </div>`;
    
    html += `<ul class="space-y-1">`;
    datos.recorrido.forEach((paso, index) => {
        html += `<li class="text-sm">
            <span class="inline-block w-6 text-gray-500">${index}</span>
            <span class="bg-gray-200 px-2 py-1 rounded font-mono text-xs mx-2">Input: ${paso.simbolo}</span>
            <span class="text-blue-600 font-mono">Estados: { ${paso.estados_activos.join(', ')} }</span>
        </li>`;
    });
    html += `</ul>`;
    return html;
}

function mostrarResultadoEj1(resultado) {
    const contenedor = document.getElementById('resultado-ej1');
    const divAfd = document.getElementById('resultado-afd-ej1');
    
    contenedor.classList.remove('hidden');
    
    if (resultado.error) {
        divAfd.innerHTML = `<p class="text-red-500">${resultado.error}</p>`;
        return;
    }

    divAfd.innerHTML = renderizarRecorrido(resultado.afd);
    
    // Cambiar color de fondo según aceptación
    divAfd.className = `p-4 rounded mt-3 border shadow-sm ${resultado.afd.aceptada ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'}`;
}

function mostrarResultadoEj2(resultado) {
    const contenedor = document.getElementById('resultado-ej2');
    const divAfd = document.getElementById('resultado-afd-ej2');
    
    contenedor.classList.remove('hidden');
    
    if (resultado.error) {
        divAfd.innerHTML = `<p class="text-red-500">${resultado.error}</p>`;
        return;
    }

    divAfd.innerHTML = renderizarRecorrido(resultado.afd);
    
    // Cambiar color de fondo según aceptación
    divAfd.className = `p-4 rounded mt-3 border shadow-sm ${resultado.afd.aceptada ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'}`;
}

function mostrarResultadoEj3(resultado) {
    const contenedor = document.getElementById('resultado-ej3');
    const divTraduccion = document.getElementById('traduccion-ej3');
    const divAfd = document.getElementById('resultado-afd-ej3');
    
    contenedor.classList.remove('hidden');
    
    if (resultado.error) {
        divTraduccion.innerHTML = '';
        divAfd.innerHTML = `<p class="text-red-500">${resultado.error}</p>`;
        return;
    }

    // Mostrar la traducción de la cadena original al alfabeto del autómata
    const datos = resultado.afd;
    divTraduccion.innerHTML = `<strong>Entrada:</strong> "${datos.cadena_original}" → <strong>Traducción:</strong> "${datos.cadena_procesada}"`;

    divAfd.innerHTML = renderizarRecorrido(datos);
    
    // Cambiar color de fondo según aceptación
    divAfd.className = `p-4 rounded mt-3 border shadow-sm ${datos.aceptada ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'}`;
}
