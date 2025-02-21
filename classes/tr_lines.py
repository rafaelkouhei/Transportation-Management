class Route:
	routes = []
	def __init__(self, cod_route, route_description, vehicle):
		self.cod_route = cod_route
		self.route_description = route_description
		self.vehicle

		Route.routes.append(self)