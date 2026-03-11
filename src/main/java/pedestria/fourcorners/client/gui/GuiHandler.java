package pedestria.fourcorners.client.gui;

import javax.annotation.Nullable;

import net.minecraft.entity.player.EntityPlayer;
import net.minecraft.tileentity.TileEntity;
import net.minecraft.util.math.BlockPos;
import net.minecraft.world.World;
import pedestria.fourcorners.client.gui.GuiCoreFabricatorSimpleContainer;
import net.minecraftforge.fml.common.network.IGuiHandler;
import pedestria.fourcorners.container.ContainerCoreFabricatorSimple;
import pedestria.fourcorners.tiles.TileEntityCoreFabricatorSimple;

public class GuiHandler implements IGuiHandler 
{
	public static final int GUI_CORE_FABRICATOR_CONTAINER_ID = 0;
	
	@Nullable
	@Override
	public Object getServerGuiElement(int ID, EntityPlayer player, World world, int x, int y, int z) {
		TileEntity te = world.getTileEntity(new BlockPos(x,y,z));
		
		switch(ID) {
			case GUI_CORE_FABRICATOR_CONTAINER_ID:
				return new ContainerCoreFabricatorSimple(player.inventory,(TileEntityCoreFabricatorSimple) te);
			default:return null;
		}
		
	}
	@Nullable
	@Override
	public Object getClientGuiElement(int ID, EntityPlayer player, World world, int x, int y, int z) {
		TileEntity te = world.getTileEntity(new BlockPos(x,y,z));
		
		switch(ID) {
			case GUI_CORE_FABRICATOR_CONTAINER_ID:
				return new GuiCoreFabricatorSimpleContainer(player.inventory, (TileEntityCoreFabricatorSimple) te);
			default:return null;
		}
	}

}
