# Generated by Django 3.1.6 on 2021-02-09 13:01

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Claims',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('vehicle_year_make', models.IntegerField(choices=[(1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)])),
                ('vehicle_model', models.CharField(max_length=100)),
                ('vehicle_number', models.CharField(max_length=100)),
                ('accident_datetime', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('loss_type', models.CharField(choices=[('Own Damage', 'Own Damage'), ('Knock for Knock', 'Knock for Knock'), ('Windscreen Damage', 'Windscreen Damage'), ('Theft', 'Theft')], max_length=17)),
                ('loss_description', models.TextField(max_length=1000)),
                ('police_report_lodged', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('anybody_injured', models.BooleanField()),
                ('photo', models.ImageField(upload_to='photos/')),
                ('pdf_document', models.FileField(upload_to='pdfs/')),
                ('claim_progress', models.CharField(choices=[('In Progress', 'In Progress'), ('Accepted', 'Accepted')], default='In Progress', max_length=11)),
            ],
        ),
    ]
