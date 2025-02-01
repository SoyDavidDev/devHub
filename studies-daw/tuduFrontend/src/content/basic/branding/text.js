module.exports = {
    "header": {
        "image": {
            "src": '/img/branding/tuduHeader.jpg',
            "alt": 'tudú!',
            "width": 500,
            "height": 500,
            "sources": [
                { "media": '(min-width: 1200px)', "srcset": '/img/web/todo/rrrepeat.svg' },
                { "media": '(min-width: 800px)', "srcset": '/img/web/todo/rrrepeat.svg' },
                { "media": '(min-width: 400px)', "srcset": '/img/web/todo/rrrepeat.svg' }
            ],
            "attrs": {notLazy: true},
            "type": 'image',
            "radius": 'rounded'
        },
        "icon": {
            "src": '/svg/icon.svg',
            "alt": 'Logo tudú!',
            "isIcon": true,
            "width": 150,
            "height": 150,
            "sources": [
                { "media": '(min-width: 1200px)', "srcset": '/svg/icon.svg' },
                { "media": '(min-width: 800px)', "srcset": '/svg/icon.svg' },
                { "media": '(min-width: 400px)', "srcset": '/svg/icon.svg' }
            ],
            "attrs": {notLazy: true},
            "type": 'icon',
            "radius": 'rounded'
        },
        "icon2": {
            "src": '/icon/favicon.ico',
            "alt": 'Logo tudú!',
            "isIcon": true,
            "width": 80,
            "height": 60,
            "sources": [
                { "media": '(min-width: 1200px)', "srcset": '/icon/favicon.ico' },
                { "media": '(min-width: 800px)', "srcset": '/icon/favicon.ico' },
                { "media": '(min-width: 400px)', "srcset": '/icon/favicon.ico' }
            ],
            "attrs": {notLazy: true},
            "type": 'icon',
            "radius": 'rounded'
        },
    },
}