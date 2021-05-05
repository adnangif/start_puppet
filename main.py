import time
import asyncio 
from pyppeteer import launch, input
from pyppeteer_stealth import stealth

approval_codes =[
    '09633219',
    '22614719',
    '99838964',
    '58907391',
    '55837784',
    '55464065',
]

print(approval_codes[3])

start_time = time.time()
async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()

    await stealth(page)
    await page.goto("https://fb.com/login")
    await page.click("#email")
    await asyncio.sleep(1)
    await page.keyboard.type('01771802195',delay=0.2)
    await page.click('#pass')
    await page.keyboard.type('fahimmarch13', delay=0.2)
    await page.click("[type~='submit']")
    await asyncio.sleep(1)
#     await asyncio.wait([
#        page.click('#approvals_code'),
#        page.waitForNavigation(),
# ])
    await page.waitForSelector("#approvals_code")
    await page.click('#approvals_code')
    await asyncio.sleep(1)
    await page.keyboard.type(approval_codes[5])
    await page.keyboard.type('\n')
    await asyncio.sleep(2)
    await page.waitForSelector("[dir~='ltr']")
    await asyncio.sleep(1)
    await page.click("[dir~='ltr']")
    await asyncio.sleep(10)
    await page.screenshot(path='bot_detect.jpg') 
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
needed_time =(time.time() - start_time)
print("time needed to complete the process: " + str(needed_time))