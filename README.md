
# Opensea metadata updater

Python bot allowing to update via a script the metadata of an Opeansea collection.

## Why ? 

By default, it is impossible to update all the metadata of a collection on Opensea. We have to do it one by one, that's what the script will do for you.


## Usage

You must start by installing the "*selenium*" library of python, it allows you to browse the web.

```python
pip install selenium
```

You have to modify **two variables** :

The variable "*collection_link*" which is a link to your opensea collection. This link must be filled in so that your link + a number returns the page of a particular NFT. 

**For example :** "https://opensea.io/assets/ethereum/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/" + 10 returns the CloneX number 10 (blockchain id).

The second variable is "*collection_supply*", it's the **number of NFT** that the script will have to update (*note: it starts from 0 and goes up to the number you have entered*).

```python
collection_link = 'https://opensea.io/assets/ethereum/addressOfYouCollection/'
collection_supply = 10
```

Once this is done, you just have to run the script .

## Authors

- [Git](https://www.github.com/0xNekr)
- [Twitter](https://www.twitter.com/0xNekr)
- [Website](https://nekr.fr)

