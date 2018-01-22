# stats.py

import falcon


# Receive input about the build process
class Build:
    def on_post(self, req, resp):
        """Handles GET requests"""
        quote = {
            'build': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = quote


# Serve statistics on the built devices
class Statistics:
    def on_get(self, req, resp):
        device = req.get_param('device') or ''
        stats = {
            'stat': {
                'device': device,
                'status': 'building',
                'last_build': '07/12/31 23:12'
            },
            'date': '12/23/45 55:33'
        }

        resp.media = stats


api = falcon.API()
api.add_route('/build', Build())
api.add_route('/stats', Statistics())
