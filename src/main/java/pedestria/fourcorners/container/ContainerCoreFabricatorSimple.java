package pedestria.fourcorners.container;

import net.minecraft.entity.player.EntityPlayer;
import net.minecraft.entity.player.InventoryPlayer;
//import net.minecraft.inventory.Slot;
import net.minecraft.util.EnumFacing;
import net.minecraftforge.items.CapabilityItemHandler;
import net.minecraftforge.items.IItemHandler;
import net.minecraftforge.items.SlotItemHandler;
import pedestria.fourcorners.container.slots.OutputSlot;
//import pedestria.fourcorners.container.slots.OutputSlot;
import pedestria.fourcorners.tiles.TileEntityCoreFabricatorSimple;

public class ContainerCoreFabricatorSimple extends ContainerMachineBase{

	public ContainerCoreFabricatorSimple(InventoryPlayer inventoryPlayer, TileEntityCoreFabricatorSimple te)
		{
			if(te.hasCapability(CapabilityItemHandler.ITEM_HANDLER_CAPABILITY, EnumFacing.NORTH)) 
			{
				IItemHandler inventory = te.getCapability(CapabilityItemHandler.ITEM_HANDLER_CAPABILITY, EnumFacing.NORTH);
				

			initPlayerInventory(inventoryPlayer);
			// MAIN FABRICATOR INVENTORY
			addSlotToContainer(new OutputSlot(inventory, 9,62 + 3*18 + 18,17 + 3*18 - 12));
			for (int y = 0; y < 3; y++) {
				for (int x = 0; x < 3; x++) {
					addSlotToContainer(new SlotItemHandler(inventory, x + (y * 3), 62 + x * 18, 17 + y * 18));
				}
			}
			
		}
	}
	@Override
	public void onContainerClosed (EntityPlayer entityPlayer) 
	{
		super.onContainerClosed(entityPlayer);
	}
}

