import asyncio
import time


async def cook_item(name, duration):
    print(f"  [Start] {name} (will take {duration}s)")
    
    
    await asyncio.sleep(duration) 
    
    print(f"  [Done]  {name} is ready!")

async def main():
    start_time = time.perf_counter()
    print("--- Breakfast Bot 3000 Starting ---\n")

    
    await asyncio.gather(
        cook_item("Boiling Egg", 5),
        cook_item("Toasting Bread", 3),
        cook_item("Pouring Juice", 1)
    )

    end_time = time.perf_counter()
    print(f"\n--- Total time elapsed: {end_time - start_time:.2f} seconds ---")


if __name__ == "__main__":
    asyncio.run(main())
