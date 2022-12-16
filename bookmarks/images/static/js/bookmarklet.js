(function () {
    var jquery_version = '3.3.1';
    var site_url = 'http://127.0.0.1:8000/';
    var static_url = site_url + 'static/';
    var min_width = 100;
    var min_height = 100;

    function bookmarklet(msg) {
        // Wczytanie stylów CSS
        var css = jQuery('<link>');
        css.attr({
            rel: 'stylesheet',
            type: 'text/css',
            href: static_url + 'css/bookmarklet.css?r=' + Math.floor(Math.random() * 9999999999999)
        });
        jQuery('head').append(css)
        // Wczytanie kodu HTML
        box_html = '<div id="bookmarklet"><a href="#" id="close">&times;</a><h1>Wybierz obraz do dodania:</h1><div class="images"></div></div>';
        jQuery('body').append(box_html);
        // Zdarzenie close
        jQuery('#bookmarklet #close').click(function () {
            jQuery('#bookmarklet').remove();
        });
        // find images and display them
        jQuery.each(jQuery('img[src$="jpg"]'), function (index, image) {
            if (jQuery(image).width() >= min_width && jQuery(image).height()
                >= min_height) {
                image_url = jQuery(image).attr('src');
                jQuery('#bookmarklet .images').append('<a href="#"><img src="' +
                    image_url + '" /></a>');
            }
        });

        // when an image is selected open URL with it
        jQuery('#bookmarklet .images a').click(function (e) {
            selected_image = jQuery(this).children('img').attr('src');
            // hide bookmarklet
            jQuery('#bookmarklet').hide();
            // open new window to submit the image
            window.open(site_url + 'images/create/?url='
                + encodeURIComponent(selected_image)
                + '&title='
                + encodeURIComponent(jQuery('title').text()),
                '_blank');
        });
    };
    // Sprawdzanie, czy biblioteka jquery została wczytana
    if (typeof window.jQuery != 'undefined') {
        bookmarklet();
    } else {
        // Sprawdzanie pod kątem konfliktów
        var conflicts = typeof window.$ != 'undefined';
        // Utworzenie skryptu i wskazanie API Google
        var script = document.createElement('script');
        script.setAttribute('src', 'http://ajax.googleapis.com/ajax/libs/jquery/' + jquery_version + '/jquery.min.js')
        // Dodanie znacznika skryptu do znacznika <head> w celu przetworzenia
        document.getElementsByTagName('head')[0].appendChild(script);
        // Zaczekaj
        var attempts = 15;
        (function () {
            // Ponowne sprawdzenie czy zdefiniowano jQuery
            if (typeof window.jQuery == 'undefined') {
                if (--attempts > 0) {
                    // Wywołanie skryptu w ciągu kilku milisekund
                    window.setTimeout(arguments.callee, 250)
                } else {
                    // Zbyt wiele prób wczytania, zgłoszenie błędu
                    alert('Wystąpił błąd podczas wczytywania jQuery')
                }
            } else {
                bookmarklet();
            }
        })();
    }
})()