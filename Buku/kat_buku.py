class rak_buku():

    def __init__(self, *args, **kwargs):
        self.__nomor_rak = kwargs.get('nomor_rak', '12')
        self.__genre_rak = kwargs.get('genre', 'komik')

    @property
    def no_rak(self):
        return self.__nomor_rak

    @no_rak.setter
    def no_rak(self, nomor_rak):
        self.__nomor_rak = nomor_rak

    @property
    def genre_rak(self):
        return self.__genre_rak

    @genre_rak.setter
    def genre_rak(self, genre_rak):
        self.__genre_rak = genre_rak

class buku():

    def __init__(self, *args, **kwargs):
        self.__id_buku = kwargs.get('id_buku', '1234')
        self.__judul_buku = kwargs.get('judul_buku', 'Haliday')
        self.__pengarang = kwargs.get('pengarang', 'albert')
        self.__penerbit = kwargs.get('penerbit', 'jogjastore')
        self.__tahun_terbit = kwargs.get('tahun_ternit', '2005')
        self.__stok_buku = kwargs.get('stok_buku', '50')
        self.__nomor_rak = kwargs.get('nomor_rak', '12')

    @property
    def id_buku(self):
        return self.__id_buku

    @id_buku.setter
    def id_buku(self, id_buku):
        self.__id_buku = id_buku

    @property
    def judul_buku(self):
        return self.__judul_buku

    @judul_buku.setter
    def judul_buku(self, judul_buku):
        self.__judul_buku = judul_buku

    @property
    def pengarang(self):
        return self.__pengarang

    @pengarang.setter
    def pengarang(self, pengarang):
        self.__pengarang = pengarang

    @property
    def penerbit(self):
        return self.__penerbit

    @penerbit.setter
    def penerbit(self, penerbit):
        self.__penerbit = penerbit

    @property
    def tahun_terbit(self):
        return self.__tahun_terbit

    @tahun_terbit.setter
    def tahun_penerbit(self, tahun_terbit):
        self.__tahun_terbit = tahun_terbit

    @property
    def stok(self):
        return self.__stok_buku

    @stok.setter
    def stok(self, stok_buku):
        self.__stok_buku = stok_buku

    @property
    def no_rak(self):
        return self.__nomor_rak

    @no_rak.setter
    def no_rak(self, nomor_rak):
        self.__nomor_rak = nomor_rak

from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///:memori', echo=True)
Base = declarative_base()

class buku(base):
    __tablename__ = "buku"

    id_buku = colum('id_buku', integer, primary_key=True)
    judul_buku = colum('judul_buku', string, unique=True)
    pengarang = colum('pengarang', string)
    penerbit = colum('penerbit', string)
    tahun_terbit = colum('tahun_ternit', string)
    stok_buku = colum('stok_buku', string)
    nomor_rak = colum('nomor_rak', integer)

    def __init__(self, id_buku, judul_buku, pengarang, penerbit, tahun_terbit, stok_buku, nomor_rak):

        self.id_buku = id_buku
        self.judul_buku = judul_buku
        self.pengarang = pengarang
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
        self.stok_buku = stok_buku
        self.nomor_rak = nomor_rak

Base.metadata.create_all(engine)





