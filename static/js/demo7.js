if ($('#trigger-overlay').length > 0) {
    (function () {

        var container = document.querySelector('div.effectSector'),
                triggerBttn = document.getElementById('trigger-overlay'),
                overlay = document.querySelector('div.menuContainer'),
                closeBttn = overlay.querySelector('a.crossButton');
        transEndEventNames = {
            'WebkitTransition': 'webkitTransitionEnd',
            'MozTransition': 'transitionend',
            'OTransition': 'oTransitionEnd',
            'msTransition': 'MSTransitionEnd',
            'transition': 'transitionend'
        },
        transEndEventName = transEndEventNames[ Modernizr.prefixed('transition') ],
                support = {transitions: Modernizr.csstransitions};

        function toggleOverlay() {
            if (classie.has(overlay, 'open')) {
                classie.remove(overlay, 'open');
                classie.remove(container, 'overlay-open');
                classie.add(overlay, 'close');
                var onEndTransitionFn = function (ev) {
                    if (support.transitions) {
                        if (ev.propertyName !== 'visibility')
                            return;
                        this.removeEventListener(transEndEventName, onEndTransitionFn);
                    }
                    classie.remove(overlay, 'close');
                };
                if (support.transitions) {
                    overlay.addEventListener(transEndEventName, onEndTransitionFn);
                }
                else {
                    onEndTransitionFn();
                }
            }
            else if (!classie.has(overlay, 'close')) {
                classie.add(overlay, 'open');
                classie.add(container, 'overlay-open');
            }
        }

        triggerBttn.addEventListener('click', toggleOverlay);
        closeBttn.addEventListener('click', toggleOverlay);
    })();
    $('#trigger-overlay,.crossButton').on('click', function (e) {
        e.preventDefault();
    });
}