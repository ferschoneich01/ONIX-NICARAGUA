        var uno = document.getElementById("uno");
        var uno_2 = document.getElementById("uno-2");
        var uno_3 = document.getElementById("uno-3");
        var dos = document.getElementById("dos");
        var dos_2 = document.getElementById("dos-2");
        var dos_3 = document.getElementById("dos-3");
        var tres = document.getElementById("tres");
        var tres_2 = document.getElementById("tres-2");
        var tres_3 = document.getElementById("tres-3");
        var cuatro = document.getElementById("cuatro");
        var cuatro_2 = document.getElementById("cuatro-2");
        var cuatro_3 = document.getElementById("cuatro-3");
        var cinco = document.getElementById("cinco");
        var cinco_2 = document.getElementById("cinco-2");
        var cinco_3 = document.getElementById("cinco-3");
        var seis = document.getElementById("seis");
        var seis_2 = document.getElementById("seis-2");
        var seis_3 = document.getElementById("seis-3");
        var siete = document.getElementById("siete");
        var siete_2 = document.getElementById("siete-2");
        var siete_3 = document.getElementById("siete-3");
        var nueve = document.getElementById("nueve");
        var nueve_2 = document.getElementById("nueve-2");
        var nueve_3 = document.getElementById("nueve-3");
        var dies = document.getElementById("dies");
        var dies_2 = document.getElementById("dies-2");
        var dies_3 = document.getElementById("dies-3");
        var once = document.getElementById("once");
        var once_2 = document.getElementById("once-2");
        var once_3 = document.getElementById("once-3");
        var doce = document.getElementById("doce");
        var doce_2 = document.getElementById("doce-2");
        var doce_3 = document.getElementById("doce-3");
        var trese = document.getElementById("trese");
        var trese_2 = document.getElementById("trese-2");
        var trese_3 = document.getElementById("trese-3");
        var catorse = document.getElementById("catorse");
        var catorse_2 = document.getElementById("catorse-2");
        var catorse_3 = document.getElementById("catorse-3");
        var quince = document.getElementById("quince");
        var quince_2 = document.getElementById("quince-2");
        var quince_3 = document.getElementById("quince-3");
        var diesiseis = document.getElementById("diesiseis");
        var diesiseis_2 = document.getElementById("diesiseis-2");
        var diesiseis_3 = document.getElementById("diesiseis-3");
        var x = false;

    document.getElementById("blanco").onclick = func;
    document.getElementById("negro").onclick = fun;
    document.getElementById("celeste").onclick = fu;
    document.getElementById("rojo").onclick = f;

    function f(){
        console.log("rojo");

        var b = document.getElementById("blanco");
        var r = document.getElementById("rojo");
        var c = document.getElementById("celeste");
        var n = document.getElementById("negro");
        b.removeEventListener("click",blanco,true);
        n.removeEventListener("click",negro,true);
        c.removeEventListener("click",celeste,true);

        r.addEventListener("click",rojo,false);

    }

    function fu(){
        console.log("celeste");

        var b = document.getElementById("blanco");
        var r = document.getElementById("rojo");
        var c = document.getElementById("celeste");
        var n = document.getElementById("negro");
        r.removeEventListener("click",rojo,true);
        n.removeEventListener("click",negro,true);
        b.removeEventListener("click",blanco,true);

        c.addEventListener("click",celeste,false);

    }

    function fun(){
        console.log("negro");

        var b = document.getElementById("blanco");
        var r = document.getElementById("rojo");
        var c = document.getElementById("celeste");
        var n = document.getElementById("negro");
        r.removeEventListener("click",rojo,true);
        b.removeEventListener("click",blanco,true);
        c.removeEventListener("click",celeste,true);

        n.addEventListener("click",negro,false);

    }

    function func(){
        console.log("blanco");

        var b = document.getElementById("blanco");
        var r = document.getElementById("rojo");
        var c = document.getElementById("celeste");
        var n = document.getElementById("negro");
        r.removeEventListener("click",rojo,true);
        n.removeEventListener("click",negro,true);
        c.removeEventListener("click",celeste,true);

        b.addEventListener("click",blanco,false);

    }


    function blanco(){
        uno.classList.add("back-blanca");
        uno_2.classList.add("back-blanca");
        uno_3.classList.add("back-blanca");
        dos.classList.add("back-blanca");
        dos_2.classList.add("back-blanca");
        dos_3.classList.add("back-blanca");
        tres.classList.add("back-blanca");
        tres_2.classList.add("back-blanca");
        tres_3.classList.add("back-blanca");
        cuatro.classList.add("back-blanca");
        cuatro_2.classList.add("back-blanca");
        cuatro_3.classList.add("back-blanca");
        cinco.classList.add("back-blanca");
        cinco_2.classList.add("back-blanca");
        cinco_3.classList.add("back-blanca");
        seis.classList.add("back-blanca");
        seis_2.classList.add("back-blanca");
        seis_3.classList.add("back-blanca");
        siete.classList.add("back-blanca");
        siete_2.classList.add("back-blanca");
        siete_3.classList.add("back-blanca");
        nueve.classList.add("back-blanca");
        nueve_2.classList.add("back-blanca");
        nueve_3.classList.add("back-blanca");
        dies.classList.add("back-blanca");
        dies_2.classList.add("back-blanca");
        dies_3.classList.add("back-blanca");
        once.classList.add("back-blanca");
        once_2.classList.add("back-blanca");
        once_3.classList.add("back-blanca");
        doce.classList.add("back-blanca");
        doce_2.classList.add("back-blanca");
        doce_3.classList.add("back-blanca");
        trese.classList.add("back-blanca");
        trese_2.classList.add("back-blanca");
        trese_3.classList.add("back-blanca");
        catorse.classList.add("back-blanca");
        catorse_2.classList.add("back-blanca");
        catorse_3.classList.add("back-blanca");
        quince.classList.add("back-blanca");
        quince_2.classList.add("back-blanca");
        quince_3.classList.add("back-blanca");
        diesiseis.classList.add("back-blanca");
        diesiseis_2.classList.add("back-blanca");
        diesiseis_3.classList.add("back-blanca");

    }

    function rojo(){
        uno.classList.add("back-rojo");
        uno_2.classList.add("back-rojo");
        uno_3.classList.add("back-rojo");
        dos.classList.add("back-rojo");
        dos_2.classList.add("back-rojo");
        dos_3.classList.add("back-rojo");
        tres.classList.add("back-rojo");
        tres_2.classList.add("back-rojo");
        tres_3.classList.add("back-rojo");
        cuatro.classList.add("back-rojo");
        cuatro_2.classList.add("back-rojo");
        cuatro_3.classList.add("back-rojo");
        cinco.classList.add("back-rojo");
        cinco_2.classList.add("back-rojo");
        cinco_3.classList.add("back-rojo");
        seis.classList.add("back-rojo");
        seis_2.classList.add("back-rojo");
        seis_3.classList.add("back-rojo");
        siete.classList.add("back-rojo");
        siete_2.classList.add("back-rojo");
        siete_3.classList.add("back-rojo");
        nueve.classList.add("back-rojo");
        nueve_2.classList.add("back-rojo");
        nueve_3.classList.add("back-rojo");
        dies.classList.add("back-rojo");
        dies_2.classList.add("back-rojo");
        dies_3.classList.add("back-rojo");
        once.classList.add("back-rojo");
        once_2.classList.add("back-rojo");
        once_3.classList.add("back-rojo");
        doce.classList.add("back-rojo");
        doce_2.classList.add("back-rojo");
        doce_3.classList.add("back-rojo");
        trese.classList.add("back-rojo");
        trese_2.classList.add("back-rojo");
        trese_3.classList.add("back-rojo");
        catorse.classList.add("back-rojo");
        catorse_2.classList.add("back-rojo");
        catorse_3.classList.add("back-rojo");
        quince.classList.add("back-rojo");
        quince_2.classList.add("back-rojo");
        quince_3.classList.add("back-rojo");
        diesiseis.classList.add("back-rojo");
        diesiseis_2.classList.add("back-rojo");
        diesiseis_3.classList.add("back-rojo");

    }

    function celeste(){
        uno.classList.add("back-celeste");
        uno_2.classList.add("back-celeste");
        uno_3.classList.add("back-celeste");
        dos.classList.add("back-celeste");
        dos_2.classList.add("back-celeste");
        dos_3.classList.add("back-celeste");
        tres.classList.add("back-celeste");
        tres_2.classList.add("back-celeste");
        tres_3.classList.add("back-celeste");
        cuatro.classList.add("back-celeste");
        cuatro_2.classList.add("back-celeste");
        cuatro_3.classList.add("back-celeste");
        cinco.classList.add("back-celeste");
        cinco_2.classList.add("back-celeste");
        cinco_3.classList.add("back-celeste");
        seis.classList.add("back-celeste");
        seis_2.classList.add("back-celeste");
        seis_3.classList.add("back-celeste");
        siete.classList.add("back-celeste");
        siete_2.classList.add("back-celeste");
        siete_3.classList.add("back-celeste");
        nueve.classList.add("back-celeste");
        nueve_2.classList.add("back-celeste");
        nueve_3.classList.add("back-celeste");
        dies.classList.add("back-celeste");
        dies_2.classList.add("back-celeste");
        dies_3.classList.add("back-celeste");
        once.classList.add("back-celeste");
        once_2.classList.add("back-celeste");
        once_3.classList.add("back-celeste");
        doce.classList.add("back-celeste");
        doce_2.classList.add("back-celeste");
        doce_3.classList.add("back-celeste");
        trese.classList.add("back-celeste");
        trese_2.classList.add("back-celeste");
        trese_3.classList.add("back-celeste");
        catorse.classList.add("back-celeste");
        catorse_2.classList.add("back-celeste");
        catorse_3.classList.add("back-celeste");
        quince.classList.add("back-celeste");
        quince_2.classList.add("back-celeste");
        quince_3.classList.add("back-celeste");
        diesiseis.classList.add("back-celeste");
        diesiseis_2.classList.add("back-celeste");
        diesiseis_3.classList.add("back-celeste");

    }

    function negro(){
        uno.classList.add("back-piedra");
        uno_2.classList.add("back-piedra");
        uno_3.classList.add("back-piedra");
        dos.classList.add("back-piedra");
        dos_2.classList.add("back-piedra");
        dos_3.classList.add("back-piedra");
        tres.classList.add("back-piedra");
        tres_2.classList.add("back-piedra");
        tres_3.classList.add("back-piedra");
        cuatro.classList.add("back-piedra");
        cuatro_2.classList.add("back-piedra");
        cuatro_3.classList.add("back-piedra");
        cinco.classList.add("back-piedra");
        cinco_2.classList.add("back-piedra");
        cinco_3.classList.add("back-piedra");
        seis.classList.add("back-piedra");
        seis_2.classList.add("back-piedra");
        seis_3.classList.add("back-piedra");
        siete.classList.add("back-piedra");
        siete_2.classList.add("back-piedra");
        siete_3.classList.add("back-piedra");
        nueve.classList.add("back-piedra");
        nueve_2.classList.add("back-piedra");
        nueve_3.classList.add("back-piedra");
        dies.classList.add("back-piedra");
        dies_2.classList.add("back-piedra");
        dies_3.classList.add("back-piedra");
        once.classList.add("back-piedra");
        once_2.classList.add("back-piedra");
        once_3.classList.add("back-piedra");
        doce.classList.add("back-piedra");
        doce_2.classList.add("back-piedra");
        doce_3.classList.add("back-piedra");
        trese.classList.add("back-piedra");
        trese_2.classList.add("back-piedra");
        trese_3.classList.add("back-piedra");
        catorse.classList.add("back-piedra");
        catorse_2.classList.add("back-piedra");
        catorse_3.classList.add("back-piedra");
        quince.classList.add("back-piedra");
        quince_2.classList.add("back-piedra");
        quince_3.classList.add("back-piedra");
        diesiseis.classList.add("back-piedra");
        diesiseis_2.classList.add("back-piedra");
        diesiseis_3.classList.add("back-piedra");

    }