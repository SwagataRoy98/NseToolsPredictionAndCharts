from django.db import models
# Create your modelss here.

class StocksHistory(models.Model):
	_companyName = models.CharField(max_length = 100,blank=True)
	_date = models.DateField()
	_open = models.DecimalField(max_digits=14, decimal_places = 7, blank = True)
	_high = models.DecimalField(max_digits=14, decimal_places = 7,blank=True)
	_low = models.DecimalField(max_digits=14, decimal_places = 7,blank=True)
	_close = models.DecimalField(max_digits=14, decimal_places = 7,blank=True)
	_adjacentClose = models.DecimalField(max_digits=14, decimal_places = 7,blank=True)
	_volume = models.BigIntegerField()

	def __str__(self):
		return r"The "+self._companyName +" had a high of "+ str(self._high)+" and a low of "+ str(self._low)+" on "+ str(self._date)  

class StocksHistoryManager(models.Manager):
	def create_record(self,_companyName,_date,_open,_high,_low,_close,_adjacentClose,_volume):
		new_record = self.create(_companyName=_companyName,_date=_date,_open=_open,_high=_high,_low=_low,_close=_close,_adjacentClose=_adjacentClose,_volume=_volume)
		return new_record