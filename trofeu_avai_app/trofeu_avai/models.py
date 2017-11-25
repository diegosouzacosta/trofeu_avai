# coding: utf-8

from django.db import models


class Jurado(models.Model):
    """
    xxx
    """
    nome = models.CharField(u'Nome completo', max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tb_jurado'
        verbose_name = 'Jurado'
        verbose_name_plural = 'Jurados'


class Jogador(models.Model):
    """
    xxx
    """
    GOLEIRO = 0
    LATERAL_DIREITO = 1
    LATERAL_ESQUERDO = 2
    ZAGUEIRO = 3
    VOLANTE = 4
    MEIA = 5
    ATACANTE = 6

    POSITIONS_CHOICES = (
        (GOLEIRO, 'Goleiro'),
        (LATERAL_DIREITO, 'Lateral direito'),
        (ZAGUEIRO, 'Zagueiro'),
        (VOLANTE, 'Volante'),
        (MEIA, 'Meia'),
        (ATACANTE, 'Atacante'),
    )

    nome = models.CharField(u'Nome completo', max_length=200)
    posicao = models.PositiveSmallIntegerField(
        choices=POSITIONS_CHOICES,
        default=GOLEIRO
    )

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tb_jogador'
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'


class Tecnico(models.Model):
    """
    xxx
    """
    nome = models.CharField(u'Nome completo', max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tb_tecnico'
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'


class Arbitro(models.Model):
    """
    xxx
    """
    nome = models.CharField(u'Nome completo', max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tb_arbitro'
        verbose_name = 'Árbitro'
        verbose_name_plural = 'Árbitros'


class Competicao(models.Model):
    """
    xxx
    """
    nome = models.CharField(u'Nome da competição', max_length=500)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tb_competicao'
        verbose_name = 'Competição'
        verbose_name_plural = 'Competições'


class Adversario(models.Model):
    """
    xxx
    """
    nome = models.CharField(u'Nome do time', max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tb_adversario'
        verbose_name = 'Adversário'
        verbose_name_plural = 'Adversários'


class Estadio(models.Model):
    """
    xxx
    """
    nome = models.CharField(u'Nome do estádio', max_length=500)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tb_estadio'
        verbose_name = 'Estádio'
        verbose_name_plural = 'Estádios'


class Jogo(models.Model):
    """
    xxx
    """
    jogadores = models.ManyToManyField(
        Jogador,
        related_name="gols",
        related_query_name="gol",
        blank=True
    )
    tecnico = models.ForeignKey(
        Tecnico,
        related_name="tecnico_jogos",
        related_query_name="tecnico_jogo"
    )
    arbitro = models.ForeignKey(
        Arbitro,
        related_name="arbitro_jogos",
        related_query_name="arbitro_jogo"
    )
    competicao = models.ForeignKey(
        Competicao,
        related_name="competicao_jogos",
        related_query_name="competicao_jogo"
    )
    adversario = models.ForeignKey(
        Adversario,
        related_name="adversario_jogos",
        related_query_name="adversario_jogo"
    )
    estadio = models.ForeignKey(
        Estadio,
        related_name="estadio_jogos",
        related_query_name="estadio_jogo"
    )

    def __str__(self):
        return self.competicao.nome

    class Meta:
        db_table = 'tb_jogo'
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'


class Gol(models.Model):
    """
    xxx
    """
    jogo = models.ForeignKey(
        Jogo,
        related_name="jogo_gols",
        related_query_name="jogo_gol"
    )
    jogador = models.ForeignKey(
        Jogador,
        related_name="jogador_gols",
        related_query_name="jogador_gol",
        blank=True,
        null=True
    )
    assistente = models.ForeignKey(
        Jogador,
        related_name="assitente_gols",
        related_query_name="assitente_gol",
        blank=True,
        null=True
    )
    minuto = models.PositiveIntegerField(unique=False, blank=True, null=True)
    finalizacao = models.CharField(
        u'Finalização', max_length=500, blank=True, null=True)
    local = models.CharField(u'Local', max_length=500, blank=True, null=True)
    origem = models.CharField(u'Origem', max_length=500, blank=True, null=True)
    data_hora = models.DateTimeField(u'Data do jogo', blank=True, null=True)

    def __str__(self):
        return self.minuto

    class Meta:
        db_table = 'tb_gol'
        verbose_name = 'Gol'
        verbose_name_plural = 'Gols'


class Nota(models.Model):
    """
    xxx
    """
    jurado = models.ForeignKey(
        Jurado,
        related_name="jurado_notas",
        related_query_name="jurado_nota"
    )
    jogo = models.ForeignKey(
        Jogo,
        related_name="jogo_notas",
        related_query_name="jogo_nota"
    )
    jogador = models.ForeignKey(
        Jogador,
        related_name="jogador_notas",
        related_query_name="jogador_nota"
    )
    nota = models.DecimalField(u'Nota', max_digits=20, decimal_places=2)

    def __str__(self):
        return self.jurado.none

    class Meta:
        db_table = 'tb_nota'
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'


class Cartao(models.Model):
    """
    xxx
    """
    AMARELO = 0
    VERMELHO = 1

    POSITIONS_CHOICES = (
        (AMARELO, 'Amarelo'),
        (VERMELHO, 'Vermelho'),
    )

    jogo = models.ForeignKey(
        Jogo,
        related_name="jogo_cartoes",
        related_query_name="jogo_cartao"
    )
    jogador = models.ForeignKey(
        Jogador,
        related_name="jogador_cartoes",
        related_query_name="jogador_cartao"
    )
    tipo = models.FloatField(u'Nota')

    def __str__(self):
        return self.jurado.none

    class Meta:
        db_table = 'tb_cartao'
        verbose_name = 'Cartão'
        verbose_name_plural = 'Cartões'
