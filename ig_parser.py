import json
import pandas as pd

# Sample JSON data
data = [
    {
        "fullName": "Spectrum Praha",
        "profilePicUrl": "https://instagram.fdnk2-1.fna.fbcdn.net/v/t51.2885-19/109236298_274276927133162_6233169972917606454_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fdnk2-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=s5FmEH0u8W4AX_BNAL3&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfCIWHLgK3xgRl8vvNGYF3P5645M0ZHwuLJxLJWYgAFZRQ&oe=6442BDAA&_nc_sid=8fd12b",
        "username": "spectrumpraha",
        "postsCount": 80,
        "followersCount": 429,
        "followsCount": 76,
        "private": False,
        "verified": False,
        "isBusinessAccount": True,
        "biography": "Softballový klub z Černého Mostu🥎\nOdkaz na náš Givt:  https://givt.cz/aplikace/sportovni-klub-spectrum-praha-z-s",
    },
    {
    "fullName": "Spectrum Praha",
    "profilePicUrl": "https://instagram.fdnk2-1.fna.fbcdn.net/v/t51.2885-19/109236298_274276927133162_6233169972917606454_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fdnk2-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=s5FmEH0u8W4AX_BNAL3&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfCIWHLgK3xgRl8vvNGYF3P5645M0ZHwuLJxLJWYgAFZRQ&oe=6442BDAA&_nc_sid=8fd12b",
    "username": "spectrumpraha",
    "postsCount": 80,
    "followersCount": 429,
    "followsCount": 76,
    "private": False,
    "verified": False,
    "isBusinessAccount": True,
    "biography": "Softballový klub z Černého Mostu🥎\nOdkaz na náš Givt:  https://givt.cz/aplikace/sportovni-klub-spectrum-praha-z-s"
  },
  {
    "fullName": "Žraloci Ledenice",
    "profilePicUrl": "https://scontent-atl3-2.cdninstagram.com/v/t51.2885-19/11005076_818506331575751_227295517_a.jpg?_nc_ht=scontent-atl3-2.cdninstagram.com&_nc_cat=111&_nc_ohc=o3ymZq1lFYsAX-x_tZ-&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfA9UALJqifpRagerQ9rJ-j7DY9nwdRQCJgOSUgTgxftlg&oe=64443D6B&_nc_sid=8fd12b",
    "username": "zraloci_ledenice",
    "postsCount": 30,
    "followersCount": 664,
    "followsCount": 106,
    "private": False,
    "verified": False,
    "isBusinessAccount": True,
    "biography": "Žraloci Ledenice jsou na instagramu! Sledujte nás a současně i žraločí hashtag ‪#‎zralociledenice‬"
  },
  {
    "fullName": "Snails Kunovice",
    "profilePicUrl": "https://scontent-cph2-1.cdninstagram.com/v/t51.2885-19/197884819_206300518010112_2396749157046500401_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-cph2-1.cdninstagram.com&_nc_cat=100&_nc_ohc=ppHPDdlRYFkAX_Sq6t3&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfBXD-zVF8eI1Z3MaCAJ1vZeOKL8P1Hm97ZtY_e7o_NXHQ&oe=64439804&_nc_sid=8fd12b",
    "username": "snailskunovice",
    "postsCount": 557,
    "followersCount": 717,
    "followsCount": 204,
    "private": False,
    "verified": False,
    "isBusinessAccount": True,
    "biography": "Softball club"
  },
  {
    "fullName": "Locos Břeclav",
    "profilePicUrl": "https://instagram.fsjk2-1.fna.fbcdn.net/v/t51.2885-19/103739491_291373242056866_4025912689430527762_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fsjk2-1.fna.fbcdn.net&_nc_cat=110&_nc_ohc=azJ2bptZPbEAX8E35Xq&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfC3NiWPOACQMiQncnL81ooNMjJMSJ-eNAuAwTqlincVew&oe=64446203&_nc_sid=8fd12b",
    "username": "breclavsoftball",
    "postsCount": 138,
    "followersCount": 992,
    "followsCount": 207,
    "private": False,
    "verified": False,
    "isBusinessAccount": True,
    "biography": "Czech fastpitch softball team 🥎\n🥇 2022 czech extraleague\n🥉 2021 czech extraleague\n🥈 2019 czech extraleague\n🥇 2018 czech 2nd league"
  },
  {
    "fullName": "Hippos Havlíčkův Brod 🥎",
    "profilePicUrl": "https://instagram.fphx2-1.fna.fbcdn.net/v/t51.2885-19/121236378_637937290443596_6549193136483686049_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fphx2-1.fna.fbcdn.net&_nc_cat=108&_nc_ohc=LCKpx_Qgf8kAX-UaMqQ&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfCU7ytWbIaQpDWrKlweC7M9HVhfoJbzjp99kxJqaH8bNA&oe=6442AB90&_nc_sid=8fd12b",
    "username": "hippos_softball",
    "postsCount": 43,
    "followersCount": 1219,
    "followsCount": 734,
    "private": False,
    "verified": False,
    "isBusinessAccount": True,
    "biography": "Fastpitch softball club 🥎 \nHavlíčkův Brod, Czech republic 🇨🇿\n- 3x🥇Czech Men´s Extraleague"
  },
  {
    "fullName": "Painbusters Most",
    "profilePicUrl": "https://instagram.fdel41-1.fna.fbcdn.net/v/t51.2885-19/18014035_1968345670051654_5009160854847881216_a.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fdel41-1.fna.fbcdn.net&_nc_cat=110&_nc_ohc=ZjkmryRq9d8AX_0homM&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfBZRaDdonb4Z5_mh6NQNVe2F6gxWLFVG8gNOjB5B7Xllg&oe=64436F0C&_nc_sid=8fd12b",
    "username": "painbusters_most",
    "postsCount": 79,
    "followersCount": 511,
    "followsCount": 78,
    "private": False,
    "verified": False,
    "isBusinessAccount": True,
    "biography": "Czech softball club 🥎\nZaložen doktory z Mostecké nemocnice roku 1989"
  },
  {
    "fullName": "SK Joudrs Praha",
    "profilePicUrl": "https://scontent-ord5-1.cdninstagram.com/v/t51.2885-19/102640314_625093301690637_5954285460108951152_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-ord5-1.cdninstagram.com&_nc_cat=109&_nc_ohc=bbfw4hBbyyQAX8bBNVA&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfBvuaIPLwPlTi6_weenYbBuLm0nDO6hEBUOl5NEHn3DQw&oe=6443480F&_nc_sid=8fd12b",
    "username": "joudrsofficial",
    "postsCount": 584,
    "followersCount": 1412,
    "followsCount": 219,
    "private": False,
    "verified": False,
    "isBusinessAccount": True,
    "biography": "⏱ Est. 1997"
  },
  {
    "fullName": "Tempo Praha",
    "profilePicUrl": "https://scontent-lax3-1.cdninstagram.com/v/t51.2885-19/54425001_378807212972157_1417887597694287872_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=MTIc-9g7mw4AX9j0ZLT&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfDgf9oeeuwvpM4eL2cP73wALVP3nFzlXCTmsILvcj6KGA&oe=64430EA3&_nc_sid=8fd12b",
    "username": "tempo_praha",
    "postsCount": 1006,
    "followersCount": 2478,
    "followsCount": 2292,
    "private": False,
    "verified": False,
    "isBusinessAccount": True,
    "biography": "⚾ Czech baseball & softball club\n🌆 Based in Prague\n⌚ Est. 1963\n#tempopraha #tempovsrdci"
  },
  {
    "fullName": "Beavers Chomutov",
    "profilePicUrl": "https://instagram.flos1-1.fna.fbcdn.net/v/t51.2885-19/107082868_3076116775817690_4673425486591705576_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.flos1-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=ksXtl6xGEIUAX8turjT&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfC2RFIeoIEuP0Zo_cT6vdh31NV4o2zc2XxwKoKy_B8W1w&oe=6442B39E&_nc_sid=8fd12b",
    "username": "beaverschomutov",
    "postsCount": 248,
    "followersCount": 809,
    "followsCount": 83,
    "private": False,
    "verified": False,
    "isBusinessAccount": True,
    "biography": "The Most Successful Men's Softball Team In Europe🏆🥎\n- 6x 🥇ECM\n- 5x 🥈ECM\n- 11x🥇Czech Men's Extraleague\n- 8x 🥈Czech Men's Extraleague"
  }
]

# Convert JSON data to a pandas DataFrame
df = pd.DataFrame(data)

# Export DataFrame to an Excel file
df.to_excel("softball_profile.xlsx", index=False)