
class Resource :

    def __init__(self,ide,canv,qte,position) :
        self.canv = canv
        self.ide = ide # id de la ressource
        self.qteinit = qte # Quantité de resssource initiale
        self.qte = qte # Quantité de ressource courante
        self.position = position # Position de la ressource
        self.res = None # Id de la ressource sur le canvas

    def affiche_resource(self) :
        """
        Crée la ressource sur le canvas
        """
        pos = self.position
        self.res = self.canv.create_oval(pos[0]-10,pos[1]-10,pos[0]+10,pos[1]+10,tag=('resource',self.ide),fill='red')
        self.canv.create_oval(pos[0]-10,pos[1]-10,pos[0]+10,pos[1]+10,outline='red')
        self.canv.addtag_withtag(self.ide,self.ide)

    def drop_resource(self):
        """
        Efface la ressource du canvas
        """
        self.canv.delete(self.ide)

    def reduce_resource(self) :
        """
        Réduis la quantité de ressources de 1 et retourne True si la ressource est vide
        """
        pos = self.position
        # cas ressource vide
        if self.qte == 0 :
            self.canv.itemconfigure(self.res,fill='',outline='')
            return True
        # cas ressource à 25%, on réduit la taille
        elif self.qte < self.qteinit//4 :
            self.canv.itemconfigure(self.res,fill='',outline='')
            self.res = self.canv.create_oval(pos[0]-3,pos[1]-3,pos[0]+3,pos[1]+3,fill='red',outline='red')
        # cas ressource à 50%, on réduit la taille
        elif self.qte < self.qteinit//2 :
            self.canv.itemconfigure(self.res,fill='',outline='')
            self.res = self.canv.create_oval(pos[0]-5,pos[1]-5,pos[0]+5,pos[1]+5,fill='red',outline='red')
        self.qte = self.qte - 1 # On réduit la quantité
        return False

    def get_pos_resource(self) :
        """
        Renvoie la position de la ressource
        """
        return self.position

    def get_ide_resource(self) :
        """
        Retourne l'id de la ressource
        """
        return self.ide
